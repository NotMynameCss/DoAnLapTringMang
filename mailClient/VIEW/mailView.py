import sys
import os
import threading
from datetime import datetime

from mailClient.VIEW.mailSendView import MailSendView
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CONTROLLER.mailController import MailController
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, Text

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

        # Create the toolbar frame
        self.toolbar_frame = tk.Frame(self.main_frame, bg="white")
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.compose_button = tk.Button(self.toolbar_frame, text="Soạn Thư", command=self.compose_email)
        self.compose_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.search_entry = tk.Entry(self.toolbar_frame, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.search_button = tk.Button(self.toolbar_frame, text="Tìm Kiếm", command=self.search_email)
        self.search_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.refresh_button = tk.Button(self.toolbar_frame, text="Làm mới", command=self.refresh_emails)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.all_emails_button = tk.Button(self.toolbar_frame, text="Tất cả Email", command=self.show_all_emails)
        self.all_emails_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create the left frame for navigation and settings/chat
        self.left_frame = tk.Frame(self.main_frame, bg="white")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.nav_frame = tk.Frame(self.left_frame, bg="white")
        self.nav_frame.grid(row=0, column=0, sticky="nsew")

        self.inbox_button = tk.Button(self.nav_frame, text="Hộp thư đến", command=self.show_inbox)
        self.inbox_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.sent_button = tk.Button(self.nav_frame, text="Đã gửi", command=self.show_sent)
        self.sent_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.drafts_button = tk.Button(self.nav_frame, text="Thư nháp", command=self.show_drafts)
        self.drafts_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.trash_button = tk.Button(self.nav_frame, text="Thùng rác", command=self.show_trash)
        self.trash_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.labels_button = tk.Button(self.nav_frame, text="Nhãn", command=self.show_labels)
        self.labels_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.settings_button = tk.Button(self.nav_frame, text="Cài đặt", command=self.show_settings)
        self.settings_button.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        self.chat_button = tk.Button(self.nav_frame, text="Chat/Meet", command=self.show_chat)
        self.chat_button.grid(row=6, column=0, padx=10, pady=5, sticky="ew")

        # Create the right frame for email list and details
        self.right_frame = tk.Frame(self.main_frame, bg="white")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.email_details_tree = ttk.Treeview(self.right_frame, columns=("From", "To", "Subject", "Date", "Body"), show="headings")
        self.email_details_tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

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

        self.email_details_tree.bind("<Double-1>", self.show_email_details)

        # Load and display emails on startup
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
        for item in self.email_details_tree.get_children():
            self.email_details_tree.delete(item)
        for email in emails:
            date_sent = email['timestamp'].strftime('%d-%m-%Y %H:%M') if isinstance(email['timestamp'], datetime) else datetime.strptime(email['timestamp'], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %H:%M')
            self.email_details_tree.insert("", "end", values=(email['sender'], email['recipients'], email['subject'], date_sent, email['body']))

    def show_email_details(self, event):
        selected_item = self.email_details_tree.selection()[0]
        email_details = self.email_details_tree.item(selected_item, "values")
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
