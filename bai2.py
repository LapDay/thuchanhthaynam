# -*- coding: utf-8 -*-
"""
họ tên: Lý Văn Lập
Mssv: 2100006075
"""
import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("AtarBals Modern Antivirus")
root.geometry("800x500")
root.configure(bg="#3b5998")

# Tạo khung chính
main_frame = tk.Frame(root, bg="#3b5998")
main_frame.pack(fill="both", expand=True)

# Tạo thanh bên
sidebar = tk.Frame(main_frame, bg="#3b5998", width=200)
sidebar.pack(side="left", fill="y")

# Tạo các nhãn trong thanh bên
labels = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
for label in labels:
    label_widget = tk.Label(sidebar, text=label, fg="white", bg="#3b5998")
    label_widget.pack(pady=10)

# Tạo nút "Scan Now"
scan_button = tk.Button(sidebar, text="Scan Now", bg="#00ff00", fg="white", command=lambda: print("Scanning..."))
scan_button.pack(pady=20)

# Tạo khu vực chính
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(side="left", fill="both", expand=True)

# Tạo tiêu đề và phụ đề
title_label = tk.Label(content_frame, text="Scan", font=("Arial", 24), bg="white")
title_label.pack(pady=20)

subtitle_label = tk.Label(content_frame, text="Premium will be free forever. You just need to click button.", bg="white")
subtitle_label.pack()

# Tạo các nút chức năng
button_frame = tk.Frame(content_frame, bg="white")
button_frame.pack(pady=20)

buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, bg="#ff00ff", fg="white")
    button.pack(side="left", padx=10)

# Tạo nhãn trạng thái
status_label = tk.Label(content_frame, text="Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)", bg="white")
status_label.pack(pady=20)

# Chạy cửa sổ
root.mainloop()