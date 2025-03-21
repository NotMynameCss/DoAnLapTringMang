import tkinter as tk
from tkinter import ttk, messagebox
from VIEW.mailSendView import MailSendView
from CONTROLLER.mailController import MailController

class MailView:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Client")
        self.root.geometry("800x600")
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

        # Create the left frame for navigation
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

        # Create the right frame for email list and details
        self.right_frame = tk.Frame(self.main_frame, bg="white")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.email_listbox = tk.Listbox(self.right_frame)
        self.email_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.email_details = tk.Text(self.right_frame, state=tk.DISABLED)
        self.email_details.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the bottom frame for settings and chat/meet
        self.bottom_frame = tk.Frame(self.main_frame, bg="white")
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.settings_button = tk.Button(self.bottom_frame, text="Cài đặt", command=self.show_settings)
        self.settings_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.chat_button = tk.Button(self.bottom_frame, text="Chat/Meet", command=self.show_chat)
        self.chat_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def compose_email(self):
        # Open the MailSendView window
        new_window = tk.Toplevel(self.root)
        MailSendView(new_window)

    def search_email(self):
        messagebox.showinfo("Search Email", "Search Email clicked")

    def show_inbox(self):
        emails = self.mail_controller.fetch_emails("inbox")
        self.display_emails(emails)

    def show_sent(self):
        emails = self.mail_controller.fetch_emails("sent")
        self.display_emails(emails)

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

    def display_emails(self, emails):
        self.email_listbox.delete(0, tk.END)
        for email in emails.split('\n'):
            self.email_listbox.insert(tk.END, email)

    def set_controller(self, controller):
        self.controller = controller

if __name__ == "__main__":
    root = tk.Tk()
    app = MailView(root)
    root.mainloop()
