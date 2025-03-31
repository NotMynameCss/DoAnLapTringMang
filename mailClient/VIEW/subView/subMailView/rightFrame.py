import tkinter as tk
from tkinter import ttk
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class RightFrame(tk.Frame):
    def __init__(self, parent, email_double_click_callback):
        super().__init__(parent, bg="white")
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Treeview hiển thị danh sách email với cột ID đầu tiên
        self.email_details_tree = ttk.Treeview(
            self, 
            columns=("ID", "From", "To", "Subject", "Date", "Body"), 
            show="headings"
        )
        self.email_details_tree.pack(fill=tk.BOTH, expand=True)

        # Cấu hình các cột
        self.email_details_tree.heading("ID", text="ID")
        self.email_details_tree.heading("From", text="From")
        self.email_details_tree.heading("To", text="To")
        self.email_details_tree.heading("Subject", text="Subject")
        self.email_details_tree.heading("Date", text="Date")
        self.email_details_tree.heading("Body", text="Body")

        self.email_details_tree.column("ID", width=50)
        self.email_details_tree.column("From", width=100)
        self.email_details_tree.column("To", width=100)
        self.email_details_tree.column("Subject", width=150)
        self.email_details_tree.column("Date", width=100)
        self.email_details_tree.column("Body", width=300)

        # Gắn sự kiện double-click
        self.email_details_tree.bind("<Double-1>", email_double_click_callback)

    def display_emails(self, emails):
        """Hiển thị danh sách email trong treeview."""
        for item in self.email_details_tree.get_children():
            self.email_details_tree.delete(item)

        for email in emails:
            # Format timestamp
            date_sent = (
                email['timestamp'].strftime('%d-%m-%Y %H:%M')
                if isinstance(email['timestamp'], datetime)
                else datetime.strptime(email['timestamp'], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %H:%M')
            )

            # Hiển thị email với ID là cột đầu tiên
            self.email_details_tree.insert("", "end", values=(
                email.get('id', ''),        # ID
                email.get('sender', ''),    # From
                email.get('recipients', ''), # To
                email.get('subject', ''),   # Subject
                date_sent,                  # Date
                email.get('body', '')       # Body
            ))

    def update_email_list(self, emails):
        """Cập nhật danh sách email trong giao diện."""
        try:
            # Xóa danh sách email cũ
            for item in self.email_details_tree.get_children():
                self.email_details_tree.delete(item)

            # Thêm email mới vào danh sách
            for email in emails:
                self.email_details_tree.insert(
                    "", "end",
                    values=(
                        email.get('id', ''),
                        email.get('sender', ''),
                        email.get('recipients', ''),
                        email.get('subject', ''),
                        email.get('timestamp', ''),
                        email.get('body', '')
                    )
                )
            logger.info(f"Cập nhật danh sách email thành công: {len(emails)} email.")
        except Exception as e:
            logger.error(f"Lỗi khi cập nhật danh sách email: {e}")
