import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CONTROLLER.mailController import MailController
import tkinter as tk
from tkinter import ttk, messagebox


class MailView:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Mail Client")
        self.root.geometry("1024x768")
        self.root.configure(background="white")

        self.mail_controller = MailController(self)

        # Create the main frame
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the top frame for search bar and new email button
        self.top_frame = tk.Frame(self.main_frame, bg="white")
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.compose_button = tk.Button(self.top_frame, text="Soạn Thư", command=self.compose_email)
        self.compose_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.search_entry = tk.Entry(self.top_frame, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.search_button = tk.Button(self.top_frame, text="Tìm Kiếm", command=self.search_email)
        self.search_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.refresh_button = tk.Button(self.top_frame, text="Làm mới", command=self.show_emails)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

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

        # Create the bottom frame for status bar
        self.status_frame = tk.Frame(self.main_frame, bg="white")
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_label = tk.Label(self.status_frame, text="Ready", bg="white")
        self.status_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Load and display emails on startup
        self.show_emails()

    def compose_email(self):
        messagebox.showinfo("Compose Email", "Compose Email clicked")

    def search_email(self):
        messagebox.showinfo("Search Email", "Search Email clicked")

    def show_inbox(self):
        messagebox.showinfo("Inbox", "Inbox clicked")

    def show_sent(self):
        messagebox.showinfo("Sent", "Sent clicked")

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
        emails = self.mail_controller.fetch_emails("inbox")
        self.display_emails(emails)

    def display_emails(self, emails):
        for item in self.email_details_tree.get_children():
            self.email_details_tree.delete(item)
        for email in emails.split('\n'):
            self.email_details_tree.insert("", "end", values=(email,))

    def set_controller(self, controller):
        self.controller = controller

if __name__ == "__main__":
    root = tk.Tk()
    app = MailView(root, "client")  # Thay thế "client" bằng tên người dùng thực tế
    root.mainloop()
