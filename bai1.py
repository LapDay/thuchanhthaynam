# -*- coding: utf-8 -*-
"""
họ tên: Lý Văn Lập
Mssv: 2100006075
"""

import tkinter as tk
from tkinter import messagebox

class FrameRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Frame Recorder")
        self.root.geometry("600x300")
        self.root.configure(bg="#d4a5a5")  # Set your preferred background color
        
        # Title label
        self.title_label = tk.Label(root, text="Frame Recorder", font=("Arial", 24, "bold"), bg="#d4a5a5")
        self.title_label.pack(pady=10)
        
        # FPS input
        self.fps_label = tk.Label(root, text="FPS (frames per second):", font=("Arial", 14), bg="#d4a5a5")
        self.fps_label.pack(pady=5)
        self.fps_entry = tk.Entry(root, font=("Arial", 14))
        self.fps_entry.pack(pady=5)
        
        # Buttons
        self.button_frame = tk.Frame(root, bg="#d4a5a5")
        self.button_frame.pack(pady=20)
        
        self.pause_button = tk.Button(self.button_frame, text="Pause", font=("Arial", 14), command=self.pause_recording)
        self.pause_button.grid(row=0, column=0, padx=10)
        
        self.start_button = tk.Button(self.button_frame, text="Start", font=("Arial", 14), command=self.start_recording)
        self.start_button.grid(row=0, column=1, padx=10)
        
        self.end_button = tk.Button(self.button_frame, text="End", font=("Arial", 14), command=self.end_recording)
        self.end_button.grid(row=0, column=2, padx=10)
        
        # Status label
        self.status_label = tk.Label(root, text="Recording Paused", font=("Arial", 14), bg="#d4a5a5")
        self.status_label.pack(pady=10)
        
    def pause_recording(self):
        self.status_label.config(text="Recording Paused")
        # Implement pause functionality here
    
    def start_recording(self):
        fps = self.fps_entry.get()
        try:
            fps = int(fps)
            self.status_label.config(text="Recording Started at {} FPS".format(fps))
            # Implement start functionality here using fps
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid FPS value")
    
    def end_recording(self):
        self.status_label.config(text="Recording Ended")
        # Implement end functionality here

if __name__ == "__main__":
    root = tk.Tk()
    app = FrameRecorder(root)
    root.mainloop()