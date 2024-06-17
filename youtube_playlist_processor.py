import os
import re
import yt_dlp
from pytube import Playlist
from openai import OpenAI

import whisper
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
import argparse
import sqlite3

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Initialize SQLite database
def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS progress (
            video_id TEXT PRIMARY KEY,
            downloaded BOOLEAN,
            transcribed BOOLEAN,
            summarized BOOLEAN,
            markdown BOOLEAN
        )
    """
    )
    conn.commit()
    return conn


# Check the progress of a video
def check_progress(cursor, video_id):
    cursor.execute("SELECT * FROM progress WHERE video_id=?", (video_id,))
    return cursor.fetchone()


# Update the progress of a video
def update_progress(
    cursor, video_id, downloaded=None, transcribed=None, summarized=None, markdown=None
):
    cursor.execute(
        "INSERT OR IGNORE INTO progress (video_id, downloaded, transcribed, summarized, markdown) VALUES (?, ?, ?, ?, ?)",
        (video_id, False, False, False, False),
    )
    if downloaded is not None:
        cursor.execute(
            "UPDATE progress SET downloaded=? WHERE video_id=?", (downloaded, video_id)
        )
    if transcribed is not None:
        cursor.execute(
            "UPDATE progress SET transcribed=? WHERE video_id=?",
            (transcribed, video_id),
        )
    if summarized is not None:
        cursor.execute(
            "UPDATE progress SET summarized=? WHERE video_id=?", (summarized, video_id)
        )
    if markdown is not None:
        cursor.execute(
            "UPDATE progress SET markdown=? WHERE video_id=?", (markdown, video_id)
        )
    cursor.connection.commit()


# Extract playlist ID and create a directory
def extract_playlist_id(url):
    match = re.search(r"list=([^&]+)", url)
    return match.group(1) if match else None


def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory


# Extract video URLs from playlist
def extract_video_urls(playlist_url):
    playlist = Playlist(playlist_url)
    return [video.watch_url for video in playlist.videos]


# Generate short URLs
def generate_short_urls(video_urls):
    return [
        url.replace("https://www.youtube.com/watch?v=", "https://youtu.be/")
        for url in video_urls
    ]


# Download audio files
def download_audio(video_url, download_dir):
    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio[ext=mp3]/bestaudio[ext=opus]",
        "outtmpl": os.path.join(download_dir, "%(id)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
                "preferredquality": "128",
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        return info["id"], info["ext"]


def download_audio_files(video_urls, download_dir, max_workers, cursor, verbose):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for url in video_urls:
            video_id = re.search(r"v=([^&]+)", url).group(1)
            # FIXME: this code has a logical flaw here. if download is finished, the video
            # will not add to future, thus skip all rest of the tasks
            # need to use a real task scheduler for this kind of work
            if (
                not check_progress(cursor, video_id)
                or not check_progress(cursor, video_id)[1]
            ):
                futures.append(executor.submit(download_audio, url, download_dir))
        results = [future.result() for future in futures]
        for video_id, ext in results:
            update_progress(cursor, video_id, downloaded=True)
            if verbose:
                print(f"Downloaded audio for video ID: {video_id}")
        return results


# Transcribe audio using Whisper
def transcribe_audio(file_path):
    model = whisper.load_model("small")
    result = model.transcribe(file_path)
    return result["text"]


def save_transcription(file_path, transcription):
    with open(file_path, "w") as f:
        f.write(transcription)


def transcribe_audio_files(audio_files, download_dir, cursor, verbose):
    for video_id, ext in audio_files:
        if not check_progress(cursor, video_id)[2]:
            audio_path = os.path.join(download_dir, f"{video_id}.{ext}")
            transcription_text = transcribe_audio(audio_path)
            transcription_file = os.path.join(
                download_dir, f"{video_id}-transcription.txt"
            )
            save_transcription(transcription_file, transcription_text)
            update_progress(cursor, video_id, transcribed=True)
            if verbose:
                print(f"Transcribed audio for video ID: {video_id}")


# Generate summary using GPT-4
def generate_summary(transcription_text, prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}:\n\n{transcription_text}"},
        ],
    )
    return completion.choices[0].message.content


def save_summary(file_path, summary):
    with open(file_path, "w") as f:
        f.write(summary)


def summarize_transcriptions(audio_files, download_dir, cursor, verbose):
    prompt = os.getenv("OPENAI_PROMPT")
    for video_id, _ in audio_files:
        if not check_progress(cursor, video_id)[3]:
            transcription_file = os.path.join(
                download_dir, f"{video_id}-transcription.txt"
            )
            with open(transcription_file, "r") as f:
                transcription_text = f.read()
            summary_text = generate_summary(transcription_text, prompt)
            summary_file = os.path.join(download_dir, f"{video_id}-summary.txt")
            save_summary(summary_file, summary_text)
            update_progress(cursor, video_id, summarized=True)
            if verbose:
                print(f"Generated summary for video ID: {video_id}")


# Generate Markdown files
def generate_markdown_files(audio_files, download_dir, markdown_dir, cursor, verbose):
    create_directory(markdown_dir)
    for video_id, _ in audio_files:
        if not check_progress(cursor, video_id)[4]:
            transcription_file = os.path.join(
                download_dir, f"{video_id}-transcription.txt"
            )
            summary_file = os.path.join(download_dir, f"{video_id}-summary.txt")
            markdown_file = os.path.join(markdown_dir, f"{video_id}.md")

            with open(transcription_file, "r") as f:
                transcription_text = f.read()
            with open(summary_file, "r") as f:
                summary_text = f.read()

            with open(markdown_file, "w") as f:
                f.write(
                    f"# Summary\n\n{summary_text}\n\n# Transcription\n\n{transcription_text}"
                )
            update_progress(cursor, video_id, markdown=True)
            if verbose:
                print(f"Generated Markdown file for video ID: {video_id}")


# Main script
def main(
    playlist_url, max_workers=1, output_dir=None, markdown_dir=None, verbose=False
):
    playlist_id = extract_playlist_id(playlist_url)
    if not playlist_id:
        print("Invalid playlist URL")
        return

    if not markdown_dir:
        print("Markdown directory is required")
        return

    download_dir = output_dir if output_dir else playlist_id
    create_directory(download_dir)

    db_path = os.path.join(".", "progress.db")
    conn = init_db(db_path)
    cursor = conn.cursor()

    video_urls = extract_video_urls(playlist_url)
    short_urls = generate_short_urls(video_urls)

    with open(os.path.join(download_dir, "playlist.txt"), "w") as f:
        f.write("\n".join(video_urls))

    with open(os.path.join(download_dir, "ytvideo.txt"), "w") as f:
        f.write("\n".join(short_urls))

    audio_files = download_audio_files(
        video_urls, download_dir, max_workers, cursor, verbose
    )
    transcribe_audio_files(audio_files, download_dir, cursor, verbose)
    summarize_transcriptions(audio_files, download_dir, cursor, verbose)
    generate_markdown_files(audio_files, download_dir, markdown_dir, cursor, verbose)

    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a YouTube playlist.")
    parser.add_argument(
        "playlist_url", type=str, help="The URL of the YouTube playlist"
    )
    parser.add_argument(
        "markdown_dir", type=str, help="The directory to save markdown files"
    )
    parser.add_argument(
        "--max_workers",
        type=int,
        default=1,
        help="The number of concurrent workers (default: 1)",
    )
    parser.add_argument(
        "--output_dir", type=str, help="The output directory (optional)", default=None
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Print progress information"
    )

    args = parser.parse_args()

    main(
        args.playlist_url,
        args.max_workers,
        args.output_dir,
        args.markdown_dir,
        args.verbose,
    )
