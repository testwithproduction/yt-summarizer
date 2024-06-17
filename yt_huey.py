import os
import re
import requests
import yt_dlp
from openai import OpenAI

import argparse
from dotenv import load_dotenv
import huey
from huey import SqliteHuey
import whisper
import torch

# Load environment variables
load_dotenv()

# Huey task manager
huey = SqliteHuey("my_app.db")

# Set OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Argument parsing
parser = argparse.ArgumentParser(description="YouTube Playlist Summarizer")
parser.add_argument("playlist_url", type=str, help="YouTube playlist URL")
parser.add_argument(
    "markdown_output_dir", type=str, help="Output directory for markdown files"
)
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

playlist_url = args.playlist_url
markdown_output_dir = args.markdown_output_dir
verbose = args.verbose


# Verbose print function
def vprint(*args):
    if verbose:
        print(*args)


# Extract playlist ID from the playlist URL
playlist_id_match = re.search(r"list=([\w-]+)", playlist_url)
if not playlist_id_match:
    raise ValueError("Invalid playlist URL")
playlist_id = playlist_id_match.group(1)
vprint(f"Extracted playlist ID: {playlist_id}")

# Create a working directory named with the playlist ID
working_dir = os.path.join(os.getcwd(), playlist_id)
os.makedirs(working_dir, exist_ok=True)
vprint(f"Created working directory: {working_dir}")


# Function to extract video URLs from the playlist
def extract_video_urls(playlist_url):
    video_urls = []
    response = requests.get(playlist_url)
    video_id_matches = re.findall(r"watch\?v=([\w-]+)", response.text)
    for video_id in set(video_id_matches):
        video_urls.append(f"https://youtu.be/{video_id}")
    return video_urls


# Function to download audio from YouTube
def download_audio(video_url, download_path):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": download_path,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "m4a"},
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"},
            {"key": "FFmpegExtractAudio", "preferredcodec": "wav"},
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    vprint(f"Downloaded audio for video: {video_url}")


# Function to transcribe audio using OpenAI Whisper API
def transcribe_audio(audio_path, transcription_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("medium", device=device)
    result = model.transcribe(audio_path)
    with open(transcription_path, "w") as f:
        f.write(result["text"])
    vprint(f"Transcribed audio: {audio_path}")


# Huey tasks
@huey.task()
def video_download_task(video_url):
    video_id = video_url.split("/")[-1]
    audio_path = os.path.join(working_dir, f"{video_id}.m4a")
    if not os.path.exists(audio_path):
        download_audio(video_url, audio_path)
        transcription_task(audio_path)
    else:
        vprint(f"Audio already downloaded for video: {video_url}")


@huey.task()
def transcription_task(audio_path):
    video_id = os.path.basename(audio_path).split(".")[0]
    transcription_path = os.path.join(working_dir, f"{video_id}-transcription.txt")
    if not os.path.exists(transcription_path):
        transcribe_audio(audio_path, transcription_path)
        summarize_task(transcription_path)
    else:
        vprint(f"Transcription already exists for audio: {audio_path}")


@huey.task()
def summarize_task(transcription_path):
    video_id = os.path.basename(transcription_path).split("-")[0]
    summary_path = os.path.join(working_dir, f"{video_id}-summary.txt")
    if not os.path.exists(summary_path):
        with open(transcription_path, "r") as file:
            transcript = file.read()
        response = client.completions.create(
            engine="gpt-4o",
            prompt=f"Summarize the following transcript:\n\n{transcript}",
            max_tokens=200,
        )
        summary = response.choices[0].text.strip()
        with open(summary_path, "w") as file:
            file.write(summary)
        vprint(f"Generated summary for transcription: {transcription_path}")
        generate_markdown_task(transcription_path, summary_path)
    else:
        vprint(f"Summary already exists for transcription: {transcription_path}")


@huey.task()
def generate_markdown_task(transcription_path, summary_path):
    video_id = os.path.basename(transcription_path).split("-")[0]
    markdown_path = os.path.join(markdown_output_dir, f"{video_id}.md")
    with open(transcription_path, "r") as trans_file:
        transcript = trans_file.read()
    with open(summary_path, "r") as summary_file:
        summary = summary_file.read()
    with open(markdown_path, "w") as md_file:
        md_file.write(f"# Summary\n\n{summary}\n\n# Transcript\n\n{transcript}")
    vprint(f"Generated markdown file: {markdown_path}")


if __name__ == "__main__":
    video_urls = extract_video_urls(playlist_url)
    vprint(f"Extracted {len(video_urls)} video URLs from playlist")
    for video_url in video_urls:
        video_download_task(video_url)
