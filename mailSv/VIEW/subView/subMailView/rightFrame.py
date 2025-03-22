import tkinter as tk
from tkinter import ttk
from datetime import datetime

class RightFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.user_listbox = tk.Listbox(self)
        self.user_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.user_listbox.bind("<<ListboxSelect>>", self.mail_view.on_user_select)

        self.user_details_tree = ttk.Treeview(self, columns=("From", "To", "Subject", "Date", "Body"), show="headings")
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

    def display_emails(self, emails):
        for item in self.user_details_tree.get_children():
            self.user_details_tree.delete(item)
        for email in emails:
            if isinstance(email.timestamp, datetime):
                date_sent = email.timestamp.strftime('%d-%m-%Y %H:%M')
            else:
                date_sent = datetime.strptime(email.timestamp, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')
            self.user_details_tree.insert("", "end", values=(email.sender, email.recipients, email.subject, date_sent, email.body))

    def display_users(self, users):
        self.user_listbox.delete(0, tk.END)
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def get_selected_user(self):
        if not self.user_listbox.curselection():
            return None
        return self.user_listbox.get(self.user_listbox.curselection())
