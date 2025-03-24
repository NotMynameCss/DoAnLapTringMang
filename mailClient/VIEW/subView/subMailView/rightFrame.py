import tkinter as tk
from tkinter import ttk, Toplevel, Text, messagebox
from datetime import datetime

class RightFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.email_details_tree = ttk.Treeview(self, columns=("From", "To", "Subject", "Date", "Body"), show="headings")
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

        self.email_details_tree.bind("<Double-1>", self.mail_view.show_email_details)

    def display_emails(self, emails):
        for item in self.email_details_tree.get_children():
            self.email_details_tree.delete(item)
        for email in emails:
            date_sent = email['timestamp'].strftime('%d-%m-%Y %H:%M') if isinstance(email['timestamp'], datetime) else datetime.strptime(email['timestamp'], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %H:%M')
            self.email_details_tree.insert("", "end", values=(email['sender'], email['recipients'], email['subject'], date_sent, email['body']))
