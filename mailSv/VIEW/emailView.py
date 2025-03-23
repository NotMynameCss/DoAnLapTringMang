import tkinter as tk
from tkinter import Text, Toplevel, ttk, messagebox
from CONTROLLER.emailController import EmailController

class EmailView:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Mail Server")
        self.root.geometry("1024x768")
        self.root.configure(background="white")

        self.email_controller = EmailController()

        # Create the main frame
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the user listbox
        self.user_listbox = tk.Listbox(self.main_frame)
        self.user_listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.user_listbox.bind("<<ListboxSelect>>", self.load_emails)

        # Create the email details treeview
        self.email_details_tree = ttk.Treeview(self.main_frame, columns=("ID", "From", "To", "Subject", "Date", "Body"), show="headings")
        self.email_details_tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

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

        self.email_details_tree.bind("<Double-1>", self.show_email_details)

        # Load users on startup
        self.load_users()

    def load_users(self):
        # Load users into the user_listbox
        users = ["user1", "user2", "user3"]  # Replace with actual user fetching logic
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def load_emails(self, event):
        selected_user = self.user_listbox.get(self.user_listbox.curselection())
        # Fetch and display emails for the selected user
        emails = self.email_controller.fetch_emails(selected_user)
        self.display_emails(emails)

    def display_emails(self, emails):
        for item in self.email_details_tree.get_children():
            self.email_details_tree.delete(item)
        for email in emails:
            self.email_details_tree.insert("", "end", values=(email['id'], email['sender'], email['recipients'], email['subject'], email['timestamp'], email['body']))

    def show_email_details(self, event):
        selected_item = self.email_details_tree.selection()[0]
        email_details = self.email_details_tree.item(selected_item, "values")
        self.open_email_details_window(email_details)

    def open_email_details_window(self, email_details):
        details_window = Toplevel(self.root)
        details_window.title("Chi tiết Email")
        details_window.geometry("600x400")

        from_label = tk.Label(details_window, text=f"From: {email_details[1]}")
        from_label.pack(anchor="w", padx=10, pady=5)

        to_label = tk.Label(details_window, text=f"To: {email_details[2]}")
        to_label.pack(anchor="w", padx=10, pady=5)

        subject_label = tk.Label(details_window, text=f"Subject: {email_details[3]}")
        subject_label.pack(anchor="w", padx=10, pady=5)

        date_label = tk.Label(details_window, text=f"Date: {email_details[4]}")
        date_label.pack(anchor="w", padx=10, pady=5)

        body_text = Text(details_window, wrap="word")
        body_text.insert("1.0", email_details[5])
        body_text.pack(fill="both", expand=True, padx=10, pady=10)
        body_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailView(root, "client")  # Replace "client" with the actual username
    root.mainloop()
