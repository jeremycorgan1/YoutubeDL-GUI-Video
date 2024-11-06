Works with linux mint cinnamon as of 11/2024
.desktop file for desktop icon
Images included to skin desktop icon and GUI
###install###
This runs from a virtual enviornment
Need python3, pilllow, tkinter, youtube-dl
##
cd into path
nano or whatever text editor to create python file, YTDL.py
nano or whatever text editor to create YTDL.desktop file
bash (to enter shell)
python3 -m venv myenv (go into venv)
source myenv/bin/activate (activate venv)
pip install youtube-dl
pip install pillow

Move YTDL.desktop to desktop
chmod +x /path/to/YTDL.py (permissions to activate)
chmod +x /path/to/YTDL.desktop (permissions to activate)
also check both file details by clicking on them to make sure is read and write and exe
