import sys
import os
import threading
from datetime import datetime
from tkinter import ttk, messagebox, Toplevel, Text
import tkinter as tk

from CONTROLLER.mailController import MailController
from VIEW.mailSendView import MailSendView
from VIEW.subView.subMailView.toolbarFrame import ToolbarFrame
from VIEW.subView.subMailView.leftFrame import LeftFrame
from VIEW.subView.subMailView.rightFrame import RightFrame

class MailView:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Mail Client")
        self.root.geometry("1024x768")
        self.root.configure(background="white")

        self.mail_controller = MailController(self.username)

        # Khung Toolbar
        self.toolbar_frame = ToolbarFrame(
            self.root,
            self.compose_email,
            self.search_email,
            self.refresh_emails,
            self.show_all_emails
        )

        # Khung bên trái
        self.left_frame = LeftFrame(
            self.root,
            self.show_inbox,
            self.show_sent,
            self.show_drafts,
            self.show_trash,
            self.show_labels,
            self.show_settings,
            self.show_chat
        )

        # Khung bên phải
        self.right_frame = RightFrame(self.root, self.show_email_details)

        # Hiển thị email khi khởi động
        self.show_emails()

    def compose_email(self):
        # Open the MailSendView window
        new_window = tk.Toplevel(self.root)
        MailSendView(new_window, self.username)

    def search_email(self):
        messagebox.showinfo("Search Email", "Search Email clicked")

    def show_inbox(self):
        threading.Thread(target=self.fetch_and_display_emails, args=("inbox",)).start()

    def show_sent(self):
        threading.Thread(target=self.fetch_and_display_emails, args=("sent",)).start()

    def show_drafts(self):
        messagebox.showinfo("Drafts", "Drafts clicked")

    def show_trash(self):
        messagebox.showinfo("Trash", "Trash clicked")

    def show_labels(self):
        messagebox.showinfo("Labels", "Labels clicked")

    def show_settings(self):
        messagebox.showinfo("Settings", "Settings clicked")

    def show_chat(self):
        messagebox.showinfo("Chat/Meet", "Chat/Meet clicked")

    def show_emails(self):
        threading.Thread(target=self.fetch_and_display_all_emails).start()

    def refresh_emails(self):
        threading.Thread(target=self.fetch_and_display_emails, args=("inbox",)).start()

    def show_all_emails(self):
        threading.Thread(target=self.fetch_and_display_all_emails).start()

    def fetch_and_display_emails(self, email_type):
        emails = self.mail_controller.fetch_emails(email_type)
        self.display_emails(emails)

    def fetch_and_display_all_emails(self):
        emails = self.mail_controller.fetch_all_emails()
        self.display_emails(emails)

    def display_emails(self, emails):
        for item in self.right_frame.email_details_tree.get_children():
            self.right_frame.email_details_tree.delete(item)
        for email in emails:
            date_sent = email['timestamp'].strftime('%d-%m-%Y %H:%M') if isinstance(email['timestamp'], datetime) else datetime.strptime(email['timestamp'], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %H:%M')
            self.right_frame.email_details_tree.insert("", "end", values=(email['sender'], email['recipients'], email['subject'], date_sent, email['body']))

    def show_email_details(self, event):
        selected_item = self.right_frame.email_details_tree.selection()[0]
        email_details = self.right_frame.email_details_tree.item(selected_item, "values")
        self.open_email_details_window(email_details)

    def open_email_details_window(self, email_details):
        details_window = Toplevel(self.root)
        details_window.title("Chi tiết Email")
        details_window.geometry("600x400")

        from_label = tk.Label(details_window, text=f"From: {email_details[0]}")
        from_label.pack(anchor="w", padx=10, pady=5)

        to_label = tk.Label(details_window, text=f"To: {email_details[1]}")
        to_label.pack(anchor="w", padx=10, pady=5)

        subject_label = tk.Label(details_window, text=f"Subject: {email_details[2]}")
        subject_label.pack(anchor="w", padx=10, pady=5)

        date_label = tk.Label(details_window, text=f"Date: {email_details[3]}")
        date_label.pack(anchor="w", padx=10, pady=5)

        body_text = Text(details_window, wrap="word")
        body_text.insert("1.0", email_details[4])
        body_text.pack(fill="both", expand=True, padx=10, pady=10)
        body_text.config(state="disabled")

    def set_controller(self, controller):
        self.controller = controller

if __name__ == "__main__":
    root = tk.Tk()
    app = MailView(root, "client")  # Thay thế "client" bằng tên người dùng thực tế
    root.mainloop()
