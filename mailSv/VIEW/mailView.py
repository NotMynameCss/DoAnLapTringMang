import datetime
import sys
import os
import threading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CONTROLLER.mailController import MailController
import tkinter as tk
from tkinter import ttk, messagebox
from loguru import logger
from VIEW.subView.subMailView.topFrame import TopFrame
from VIEW.subView.subMailView.leftFrame import LeftFrame
from VIEW.subView.subMailView.rightFrame import RightFrame

class MailView:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Mail Server")
        self.root.geometry("1024x768")
        self.root.configure(background="white")

        self.mail_controller = MailController()

        # Create the main frame
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the top frame for search bar and new email button
        self.top_frame = TopFrame(self.main_frame, self)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create the left frame for navigation and settings/chat
        self.left_frame = LeftFrame(self.main_frame, self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the right frame for user list and details
        self.right_frame = RightFrame(self.main_frame, self)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Load and display users on startup
        self.show_users()

    def compose_email(self):
        messagebox.showinfo("Soạn Thư", "Chức năng soạn thư chưa được triển khai")

    def search_email(self):
        query = self.top_frame.search_entry.get()
        emails = self.mail_controller.search_emails(query)
        self.right_frame.display_emails(emails)

    def show_inbox(self):
        threading.Thread(target=self.fetch_and_display_emails, args=("inbox",)).start()

    def show_sent(self):
        threading.Thread(target=self.fetch_and_display_emails, args=("sent",)).start()

    def show_drafts(self):
        messagebox.showinfo("Thư nháp", "Chức năng thư nháp chưa được triển khai")

    def show_trash(self):
        messagebox.showinfo("Thùng rác", "Chức năng thùng rác chưa được triển khai")

    def show_labels(self):
        messagebox.showinfo("Nhãn", "Chức năng nhãn chưa được triển khai")

    def show_settings(self):
        messagebox.showinfo("Cài đặt", "Chức năng cài đặt chưa được triển khai")

    def show_chat(self):
        messagebox.showinfo("Chat/Meet", "Chức năng Chat/Meet chưa được triển khai")

    def show_users(self):
        users = self.mail_controller.fetch_all_users()
        self.right_frame.display_users(users)

    def fetch_and_display_emails(self, email_type):
        emails = self.mail_controller.fetch_emails(email_type)
        self.right_frame.display_emails(emails)

    def refresh_emails(self):
        selected_user = self.get_selected_user()
        if selected_user:
            emails = self.mail_controller.fetch_emails_by_user(selected_user, "inbox")
            self.right_frame.display_emails(emails)
        else:
            messagebox.showinfo("Thông báo", "Vui lòng chọn người dùng để làm mới danh sách email.")

    def get_selected_user(self):
        return self.right_frame.get_selected_user()

    def set_controller(self, controller):
        self.controller = controller

    def on_user_select(self, event):
        selected_user = self.get_selected_user()
        if selected_user:
            emails = self.mail_controller.fetch_emails_by_user(selected_user)
            self.right_frame.display_emails(emails)
