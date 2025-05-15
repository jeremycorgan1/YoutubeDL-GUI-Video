# YTDL - YouTube Video Downloader

A simple GUI tool to download YouTube videos using `yt-dlp`.

## Prerequisites
- Python 3.12 or later
- `tkinter` (usually included with Python, but may need to be installed separately, e.g., `sudo apt install python3-tk` on Debian/Ubuntu-based systems)

## Installation
1. Clone this repository:
https://github.com/jeremycorgan1/YoutubeDL-GUI-Video.git

2. Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. (Optional) Set up the desktop entry for easy launching:
- Copy `YTDL.desktop` to your applications directory:
cp YTDL.desktop ~/.local/share/applications/
(i had to systemwide install with sudo ####sudo cp YTDL.desktop /usr/share/applications/)

- Update the `Exec` and `Icon` paths in `YTDL.desktop` to match your system:

Exec=/path/to/ytdl-tool/ytdl.py
Icon=/path/to/ytdl-tool/asuka.png

- Note: You might need to make `ytdl.py` executable: `chmod +x ytdl.py` (this was needed for me to make work on my linux mint machine)

## Usage
1. Run the tool:

python3 ytdl.py

Or, if you set up the desktop entry, launch "YTDL" from your application menu.
2. Enter a YouTube URL, choose a download path, and click "Download Video".

## Notes
- Ensure `asuka.png` and `chibiytdl.png` are in the same directory as `ytdl.py`, or update the paths in `ytdl.py` accordingly.
- This tool requires an internet connection to download videos.

