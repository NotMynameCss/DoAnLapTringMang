import sys
import os
import threading
from datetime import datetime
from tkinter import ttk, messagebox, Toplevel, Text
import tkinter as tk

from loguru import logger

from CONTROLLER.mailController import MailController
from VIEW.mailSendView import MailSendView
from VIEW.subView.subMailView.toolbarFrame import ToolbarFrame
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

        # Khung Toolbar
        self.toolbar_frame = ToolbarFrame(
            self.root,
            self.compose_email,
            self.search_email,
            self.refresh_emails,
            self.show_all_emails,
            self.logout  # Thêm callback logout
        )

        # Khung bên trái
        self.left_frame = LeftFrame(
            self.root,
            self.show_inbox,
            self.show_sent,
            self.show_drafts,
            self.show_trash,
            self.show_labels,
            self.show_settings,
            self.show_chat,
            self.delete_email  # Thêm callback cho nút Xóa Mail
        )

        # Khung bên phải
        self.right_frame = RightFrame(self.root, self.show_email_details)

        # Hiển thị email khi khởi động
        self.show_emails()

    def compose_email(self):
        # Mở cửa sổ soạn mail và truyền callback làm mới
        new_window = tk.Toplevel(self.root)
        MailSendView(new_window, self.username, refresh_callback=self.refresh_emails)

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
        """Làm mới danh sách email từ máy chủ."""
        try:
            threading.Thread(target=self.fetch_and_display_emails, args=("inbox",)).start()
            logger.info("Đã gửi yêu cầu làm mới danh sách email.")
        except Exception as e:
            logger.error(f"Lỗi khi làm mới danh sách email: {e}")
            messagebox.showerror("Lỗi", "Không thể làm mới danh sách email. Vui lòng thử lại sau.")

    def show_all_emails(self):
        threading.Thread(target=self.fetch_and_display_all_emails).start()

    def fetch_and_display_emails(self, email_type):
        emails = self.mail_controller.fetch_emails(email_type)
        self.display_emails(emails)

    def fetch_and_display_all_emails(self):
        emails = self.mail_controller.fetch_all_emails()
        self.display_emails(emails)

    def display_emails(self, emails):
        """Hiển thị danh sách email"""
        for item in self.right_frame.email_details_tree.get_children():
            self.right_frame.email_details_tree.delete(item)
            
        for email in emails:
            # Định dạng ngày tháng
            date_sent = (
                email['timestamp'].strftime('%d-%m-%Y %H:%M')
                if isinstance(email['timestamp'], datetime)
                else datetime.strptime(email['timestamp'], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %H:%M')
            )
            
            # Thêm email với ID là cột đầu tiên
            self.right_frame.email_details_tree.insert("", "end", values=(
                email.get('id', ''),        # ID 
                email.get('sender', ''),    # From
                email.get('recipients', ''), # To
                email.get('subject', ''),   # Subject
                date_sent,                  # Date
                email.get('body', '')       # Body
            ))

    def show_email_details(self, event):
        selected_item = self.right_frame.email_details_tree.selection()[0]
        email_details = self.right_frame.email_details_tree.item(selected_item, "values")
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

    def delete_email(self):
        """Xóa email được chọn và làm mới giao diện."""
        try:
            selected_item = self.right_frame.email_details_tree.selection()
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

            # Gửi yêu cầu xóa email
            response = self.mail_controller.delete_email(email_id)
            if response.get("success"):
                messagebox.showinfo("Thành công", response.get("message", "Đã xóa email"))
                # Làm mới giao diện sau khi xóa
                self.refresh_emails()
            else:
                messagebox.showerror("Lỗi", response.get("message", "Không thể xóa email"))

        except Exception as e:
            logger.error(f"Lỗi khi xóa email: {e}")
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi khi xóa email")

    def _get_email_id_from_tree(self, item) -> int:
        """Lấy email ID từ tree item một cách an toàn"""
        try:
            values = self.right_frame.email_details_tree.item(item)["values"]
            if not values:
                logger.error("Không có dữ liệu trong tree item")
                return None
                
            email_id = values[0]  # ID là cột đầu tiên
            if not email_id:
                logger.error("Email ID rỗng")
                return None
                
            return int(email_id)
            
        except (IndexError, TypeError, ValueError) as e:
            logger.error(f"Lỗi khi lấy email ID: {str(e)}")
            return None

    def _confirm_delete(self) -> bool:
        """Hiển thị dialog xác nhận xóa"""
        return messagebox.askyesno(
            "Xác nhận", 
            "Bạn có chắc chắn muốn xóa email này không?"
        )

    def logout(self):
        """Đăng xuất user hiện tại và quay lại màn hình đăng nhập"""
        try:
            # Gửi thông báo đăng xuất về server
            try:
                self.mail_controller.send_request(f"LOGOUT {self.username}")
            except Exception as e:
                logger.warning(f"Không thể gửi thông báo LOGOUT về server: {e}")
            from VIEW.authView import AuthView
            # Ghi log sự kiện đăng xuất local
            logger.info(f"User '{self.username}' đã đăng xuất khỏi mailClient.")
            # Xóa toàn bộ widget trong root
            for widget in self.root.winfo_children():
                widget.destroy()
            # Hiển thị lại giao diện đăng nhập
            AuthView(self.root).show_auth()
        except Exception as e:
            from tkinter import messagebox
            logger.error(f"Lỗi khi đăng xuất user '{self.username}': {e}")
            messagebox.showerror("Lỗi", f"Không thể đăng xuất: {e}")

    def set_controller(self, controller):
        self.controller = controller

if __name__ == "__main__":
    root = tk.Tk()
    app = MailView(root, "client")  # Thay thế "client" bằng tên người dùng thực tế
    root.mainloop()
