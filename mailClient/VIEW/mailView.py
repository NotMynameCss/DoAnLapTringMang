import sys
import os
import threading
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CONTROLLER.mailController import MailController
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, Text
from VIEW.mailSendView import MailSendView
from VIEW.subView.subMailView.topFrame import TopFrame
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

        # Create the main frame
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the top frame for search bar and new email button
        self.top_frame = TopFrame(self.main_frame, self)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create the left frame for navigation and settings/chat
        self.left_frame = LeftFrame(self.main_frame, self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the right frame for email list and details
        self.right_frame = RightFrame(self.main_frame, self)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Load and display emails on startup
        self.show_emails()

    def compose_email(self):
        # Open the MailSendView window
        new_window = tk.Toplevel(self.root)
        MailSendView(new_window, self.username)

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

    def show_emails(self):
        threading.Thread(target=self.fetch_and_display_all_emails).start()

    def refresh_emails(self):
        threading.Thread(target=self.fetch_and_display_emails, args=("inbox",)).start()

    def show_all_emails(self):
        threading.Thread(target=self.fetch_and_display_all_emails).start()

    def fetch_and_display_emails(self, email_type):
        emails = self.mail_controller.fetch_emails(email_type)
        self.right_frame.display_emails(emails)

    def fetch_and_display_all_emails(self):
        emails = self.mail_controller.fetch_all_emails()
        self.right_frame.display_emails(emails)

    def display_emails(self, emails):
        self.right_frame.display_emails(emails)

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
