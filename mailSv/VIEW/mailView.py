import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CONTROLLER.mailController import MailController
import tkinter as tk
from tkinter import ttk, messagebox

class MailView:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Server")
        self.root.geometry("1024x768")
        self.root.configure(background="white")

        self.mail_controller = MailController()

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

        self.refresh_button = tk.Button(self.top_frame, text="Làm mới", command=self.refresh_emails)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create the left frame for navigation and settings/chat
        self.left_frame = tk.Frame(self.main_frame, bg="white")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.inbox_button = tk.Button(self.left_frame, text="Hộp thư đến", command=self.show_inbox)
        self.inbox_button.pack(fill=tk.X, padx=10, pady=5)

        self.sent_button = tk.Button(self.left_frame, text="Đã gửi", command=self.show_sent)
        self.sent_button.pack(fill=tk.X, padx=10, pady=5)

        self.drafts_button = tk.Button(self.left_frame, text="Thư nháp", command=self.show_drafts)
        self.drafts_button.pack(fill=tk.X, padx=10, pady=5)

        self.trash_button = tk.Button(self.left_frame, text="Thùng rác", command=self.show_trash)
        self.trash_button.pack(fill=tk.X, padx=10, pady=5)

        self.labels_button = tk.Button(self.left_frame, text="Nhãn", command=self.show_labels)
        self.labels_button.pack(fill=tk.X, padx=10, pady=5)

        self.settings_button = tk.Button(self.left_frame, text="Cài đặt", command=self.show_settings)
        self.settings_button.pack(fill=tk.X, padx=10, pady=5)

        self.chat_button = tk.Button(self.left_frame, text="Chat/Meet", command=self.show_chat)
        self.chat_button.pack(fill=tk.X, padx=10, pady=5)

        # Create the right frame for user list and details
        self.right_frame = tk.Frame(self.main_frame, bg="white")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.user_listbox = tk.Listbox(self.right_frame)
        self.user_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.user_listbox.bind("<<ListboxSelect>>", self.on_user_select)

        self.user_details_tree = ttk.Treeview(self.right_frame, columns=("From", "To", "Subject", "Date", "Body"), show="headings")
        self.user_details_tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.user_details_tree.heading("From", text="From")
        self.user_details_tree.heading("To", text="To")
        self.user_details_tree.heading("Subject", text="Subject")
        self.user_details_tree.heading("Date", text="Date")
        self.user_details_tree.heading("Body", text="Body")

        self.user_details_tree.column("From", width=100)
        self.user_details_tree.column("To", width=100)
        self.user_details_tree.column("Subject", width=150)
        self.user_details_tree.column("Date", width=100)
        self.user_details_tree.column("Body", width=300)

        # Load and display users on startup
        self.show_users()

    def compose_email(self):
        messagebox.showinfo("Soạn Thư", "Chức năng soạn thư chưa được triển khai")

    def search_email(self):
        query = self.search_entry.get()
        emails = self.mail_controller.search_emails(query)
        self.display_emails(emails)

    def show_inbox(self):
        emails = self.mail_controller.fetch_emails("inbox")
        self.display_emails(emails)

    def show_sent(self):
        emails = self.mail_controller.fetch_emails("sent")
        self.display_emails(emails)

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
        self.display_users(users)

    def refresh_emails(self):
        emails = self.mail_controller.fetch_all_emails()
        self.display_emails(emails)

    def display_emails(self, emails):
        for item in self.user_details_tree.get_children():
            self.user_details_tree.delete(item)
        for email in emails:
            if isinstance(email['timestamp'], datetime.datetime):
                date_sent = email['timestamp'].strftime('%d-%m-%Y %H:%M')
            else:
                date_sent = datetime.datetime.strptime(email['timestamp'], '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')
            self.user_details_tree.insert("", "end", values=(email['sender'], email['recipients'], email['subject'], date_sent, email['body']))

    def display_users(self, users):
        self.user_listbox.delete(0, tk.END)
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def on_user_select(self, event):
        if not self.user_listbox.curselection():
            return
        selected_user = self.user_listbox.get(self.user_listbox.curselection())
        emails = self.mail_controller.fetch_emails_by_user(selected_user)
        self.display_emails(emails)

    def set_controller(self, controller):
        self.controller = controller

if __name__ == "__main__":
    root = tk.Tk()
    app = MailView(root)
    root.mainloop()
