import os
import shutil
from pathlib import Path
import tkinter as tk

def organize_files_by_extension(source_dir, target_dir):
    print('Hello World')

def sd_pull():
    print('Pulling latest videos...')

def youtube_download():
    print('Downloading videos from YouTube...')

def create_gui():
    root = tk.Tk()
    root.title("File Organizer")

    source_label = tk.Label(root, text="Source Directory:")
    source_label.pack()
    source_entry = tk.Entry(root)
    source_entry.pack()

    target_label = tk.Label(root, text="Target Directory:")
    target_label.pack()
    target_entry = tk.Entry(root)
    target_entry.pack()

    organize_button = tk.Button(root, text="Organize Files", command=lambda: organize_files_by_extension(source_entry.get(), target_entry.get()))
    organize_button.pack()

    sd_pull_button = tk.Button(root, text="SD Pull", command=sd_pull)
    sd_pull_button.pack()

    youtube_download_button = tk.Button(root, text="YouTube Download", command=youtube_download)
    youtube_download_button.pack()

    root.mainloop()