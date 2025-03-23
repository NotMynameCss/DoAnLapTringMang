import tkinter as tk
from tkinter import ttk, Toplevel, Text, messagebox
from datetime import datetime
from loguru import logger

class RightFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.user_listbox = tk.Listbox(self)
        self.user_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.user_listbox.bind("<<ListboxSelect>>", self.mail_view.on_user_select)

        self.user_details_tree = ttk.Treeview(self, columns=("ID", "From", "To", "Subject", "Date", "Body"), show="headings")
        self.user_details_tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.user_details_tree.heading("ID", text="ID")
        self.user_details_tree.heading("From", text="From")
        self.user_details_tree.heading("To", text="To")
        self.user_details_tree.heading("Subject", text="Subject")
        self.user_details_tree.heading("Date", text="Date")
        self.user_details_tree.heading("Body", text="Body")

        self.user_details_tree.column("ID", width=50)
        self.user_details_tree.column("From", width=100)
        self.user_details_tree.column("To", width=100)
        self.user_details_tree.column("Subject", width=150)
        self.user_details_tree.column("Date", width=100)
        self.user_details_tree.column("Body", width=300)

        self.user_details_tree.bind("<Double-1>", self.show_email_details)

    def display_emails(self, emails):
        for item in self.user_details_tree.get_children():
            self.user_details_tree.delete(item)
        for email in emails:
            if isinstance(email.timestamp, datetime):
                date_sent = email.timestamp.strftime('%d-%m-%Y %H:%M')
            else:
                date_sent = datetime.strptime(email.timestamp, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')
            self.user_details_tree.insert("", "end", values=(email.id, email.sender, email.recipients, email.subject, date_sent, email.body))

    def display_users(self, users):
        self.user_listbox.delete(0, tk.END)
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def get_selected_user(self):
        if not self.user_listbox.curselection():
            return None
        return self.user_listbox.get(self.user_listbox.curselection())

    def show_email_details(self, event):
        selected_item = self.user_details_tree.selection()[0]
        email_id = self.user_details_tree.item(selected_item, "values")[0]
        logger.info(f"Selected email ID: {email_id}")
        email_details = self.mail_view.mail_controller.fetch_email_details(email_id)
        if email_details:
            self.open_email_details_window(email_details)
        else:
            messagebox.showerror("Error", f"Không tìm thấy email với ID: {email_id}")

    def open_email_details_window(self, email_details):
        details_window = Toplevel(self)
        details_window.title("Chi tiết Email")
        details_window.geometry("600x400")

        from_label = tk.Label(details_window, text=f"From: {email_details.get('sender', 'N/A')}")
        from_label.pack(anchor="w", padx=10, pady=5)

        to_label = tk.Label(details_window, text=f"To: {email_details.get('recipients', 'N/A')}")
        to_label.pack(anchor="w", padx=10, pady=5)

        subject_label = tk.Label(details_window, text=f"Subject: {email_details.get('subject', 'N/A')}")
        subject_label.pack(anchor="w", padx=10, pady=5)

        date_label = tk.Label(details_window, text=f"Date: {email_details.get('timestamp', 'N/A')}")
        date_label.pack(anchor="w", padx=10, pady=5)

        body_text = Text(details_window, wrap="word")
        body_text.insert("1.0", email_details.get('body', 'N/A'))
        body_text.pack(fill="both", expand=True, padx=10, pady=10)
        body_text.config(state="disabled")
