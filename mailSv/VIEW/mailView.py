import datetime
import sys
import os
import threading
from typing import Optional
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CONTROLLER.mailController import MailController
import tkinter as tk
from tkinter import ttk, messagebox
from loguru import logger
from VIEW.subView.subMailView.topFrame import TopFrame
from VIEW.subView.subMailView.leftFrame import LeftFrame
from VIEW.subView.subMailView.rightFrame import RightFrame
from VIEW.mailSendView import MailSendView  # Import MailSendView


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

    def show_users(self):
        users = self.mail_controller.fetch_all_users()
        self.right_frame.display_users(users)

    def fetch_and_display_emails(self, email_type):
        emails = self.mail_controller.fetch_emails(email_type)
        self.right_frame.display_emails(emails)

    def refresh_emails(self):
        selected_user = self.get_selected_user()
        if (selected_user):
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

    def fetch_email_details(self, email_id):
        return self.mail_controller.fetch_email_details(email_id)

    def delete_email(self):
        """Xóa email được chọn"""
        try:
            selected_item = self.right_frame.user_details_tree.selection()
            if not selected_item:
                messagebox.showwarning("Xóa Mail", "Vui lòng chọn email để xóa")
                return

            # Lấy email ID từ tree view
            email_id = self._get_email_id_from_tree(selected_item[0])
            if not email_id:
                messagebox.showerror("Lỗi", "Không thể xác định email cần xóa")
                return

            # Xác nhận xóa
            if not self._confirm_delete():
                return

            # Gọi API xóa email
            response = self.mail_controller.delete_email(email_id, self.username)
            
            if not isinstance(response, dict):
                raise ValueError("Invalid response format")

            if response.get("success"):
                messagebox.showinfo("Thành công", response.get("message", "Đã xóa email"))
                self.refresh_emails()
            else:
                messagebox.showerror("Lỗi", response.get("message", "Không thể xóa email"))

        except Exception as e:
            logger.error(f"Lỗi khi xóa email: {e}")
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi khi xóa email")
            
    def _get_email_id_from_tree(self, item) -> Optional[int]:
        """Lấy email ID từ tree item"""
        try:
            values = self.right_frame.user_details_tree.item(item)["values"]
            return int(values[0]) if values else None
        except (IndexError, ValueError):
            return None

    def _confirm_delete(self) -> bool:
        """Hiển thị dialog xác nhận xóa"""
        return messagebox.askyesno(
            "Xác nhận", 
            "Bạn có chắc chắn muốn xóa email này không?"
        )
