# YouTube Playlist Processor

This project processes a YouTube playlist to extract audio, transcribe it, generate summaries, and create Markdown files.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository or download the script.

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory with the following content:

    ```ini
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_PROMPT="Summarize the following transcription:"
    ```

## Usage

Run the script with the following command:

```bash
python youtube_playlist_processor.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" 4 --output_dir /path/to/output --markdown_dir /path/to/markdown --verbose
