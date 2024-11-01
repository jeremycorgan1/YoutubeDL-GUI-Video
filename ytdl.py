import os
import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Video Downloader")
        self.geometry("500x400")
        
        # Initialize variables
        self.download_path = tk.StringVar()
        self.download_path.set(os.path.expanduser("~"))  # Default path
        
        # Set up background image label
        self.background_label = tk.Label(self)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Hardcoded background image path
        self.background_image_path = "/home/oem/Downloads/54abl.jpg"  # Replace with your image path
        self.load_background_image()  # Load the background image on startup
        
        # Create UI components directly on the main window
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter YouTube URL:", bg="lightgrey").pack(pady=5)
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        tk.Label(self, text="Download Path:", bg="lightgrey").pack(pady=5)
        tk.Entry(self, textvariable=self.download_path, width=50).pack(pady=5)
        path_button = tk.Button(self, text="Choose Folder", command=self.choose_path, bg="lightgrey")
        path_button.pack(pady=5)

        download_button = tk.Button(self, text="Download Video", command=self.download_video, bg="lightgrey")
        download_button.pack(pady=20)

        self.status_label = tk.Label(self, text="", wraplength=400, bg="lightgrey")
        self.status_label.pack(pady=10)

    def load_background_image(self):
        """Load the background image from the hardcoded path."""
        if os.path.exists(self.background_image_path):
            try:
                img = Image.open(self.background_image_path)
                bg_img = ImageTk.PhotoImage(img.resize((500, 400), Image.LANCZOS))
                self.background_label.config(image=bg_img)
                self.background_label.image = bg_img  # Keep a reference to avoid garbage collection
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load background image: {e}")
        else:
            messagebox.showerror("Error", f"Background image not found at {self.background_image_path}")

    def choose_path(self):
        path = filedialog.askdirectory()
        if path:
            self.download_path.set(path)

    def download_video(self):
        url = self.url_entry.get()
        path = self.download_path.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return

        if not os.path.exists(path):
            messagebox.showerror("Error", "Download path does not exist.")
            return

        self.status_label.config(text="Downloading video...")

        ydl_opts = {
            'format': 'best',  # Downloads the best video+audio quality available
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        }
        
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.config(text="Video downloaded successfully!")
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")
            self.status_label.config(text="")

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()

