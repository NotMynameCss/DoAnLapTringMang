import tkinter as tk
from tkinter import ttk

class RightFrame(tk.Frame):
    def __init__(self, parent, email_double_click_callback):
        super().__init__(parent, bg="white")
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Treeview hiển thị danh sách email
        self.email_details_tree = ttk.Treeview(self, columns=("From", "To", "Subject", "Date", "Body"), show="headings")
        self.email_details_tree.pack(fill=tk.BOTH, expand=True)

        # Cấu hình các cột
        self.email_details_tree.heading("From", text="From")
        self.email_details_tree.heading("To", text="To")
        self.email_details_tree.heading("Subject", text="Subject")
        self.email_details_tree.heading("Date", text="Date")
        self.email_details_tree.heading("Body", text="Body")

        self.email_details_tree.column("From", width=100)
        self.email_details_tree.column("To", width=100)
        self.email_details_tree.column("Subject", width=150)
        self.email_details_tree.column("Date", width=100)
        self.email_details_tree.column("Body", width=300)

        # Gắn sự kiện double-click
        self.email_details_tree.bind("<Double-1>", email_double_click_callback)
