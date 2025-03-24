import tkinter as tk
from tkinter import ttk, Toplevel, Text, messagebox
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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

        self.user_details_tree.bind("<Double-1>", self.show_email_details)

    def display_emails(self, emails):
        """Hiển thị danh sách email trong treeview"""
        for item in self.user_details_tree.get_children():
            self.user_details_tree.delete(item)
        for email in emails:
            if isinstance(email.timestamp, datetime):
                date_sent = email.timestamp.strftime('%d-%m-%Y %H:%M')
            else:
                date_sent = datetime.strptime(email.timestamp, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')
            # Thêm ID vào values của tree item
            self.user_details_tree.insert("", "end", values=(
                email.id,  # Đảm bảo ID được thêm vào đầu tiên
                email.sender, 
                email.recipients, 
                email.subject, 
                date_sent, 
                email.body
            ))

    def display_users(self, users):
        self.user_listbox.delete(0, tk.END)
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def get_selected_user(self):
        if not self.user_listbox.curselection():
            return None
        return self.user_listbox.get(self.user_listbox.curselection())

    def show_email_details(self, event):
        """Hiển thị chi tiết email khi double click"""
        try:
            if not self.user_details_tree.selection():
                logger.warning("Không có email nào được chọn")
                return
            
            selected_item = self.user_details_tree.selection()[0]
            values = self.user_details_tree.item(selected_item)['values']
            
            if not values:
                logger.warning("Không có dữ liệu email được chọn")
                return
            
            email_id = values[0]  # ID là giá trị đầu tiên trong values
            logger.debug(f"Đang lấy chi tiết email ID: {email_id}")
            
            email_details = self.mail_view.fetch_email_details(email_id)
            
            if email_details:
                self.open_email_details_window(email_details)
            else:
                messagebox.showerror("Lỗi", f"Không thể tải chi tiết email ID: {email_id}")
                
        except Exception as e:
            logger.error(f"Lỗi khi hiển thị chi tiết email: {str(e)}")
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi khi hiển thị chi tiết email")

    def open_email_details_window(self, email_details):
        """Mở cửa sổ hiển thị chi tiết email"""
        try:
            details_window = Toplevel(self)
            details_window.title("Chi tiết Email")
            details_window.geometry("600x400")

            # Thêm scrollbar
            main_frame = ttk.Frame(details_window)
            main_frame.pack(fill=tk.BOTH, expand=True)

            canvas = tk.Canvas(main_frame)
            scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            # Hiển thị thông tin email
            ttk.Label(scrollable_frame, text=f"From: {email_details['sender']}").pack(anchor="w", padx=10, pady=5)
            ttk.Label(scrollable_frame, text=f"To: {email_details['recipients']}").pack(anchor="w", padx=10, pady=5)
            
            if email_details.get('cc'):
                ttk.Label(scrollable_frame, text=f"CC: {email_details['cc']}").pack(anchor="w", padx=10, pady=5)
            if email_details.get('bcc'):
                ttk.Label(scrollable_frame, text=f"BCC: {email_details['bcc']}").pack(anchor="w", padx=10, pady=5)
                
            ttk.Label(scrollable_frame, text=f"Subject: {email_details['subject']}").pack(anchor="w", padx=10, pady=5)
            ttk.Label(scrollable_frame, text=f"Date: {email_details['timestamp']}").pack(anchor="w", padx=10, pady=5)

            # Text widget cho nội dung email
            body_text = Text(scrollable_frame, wrap="word", height=10)
            body_text.insert("1.0", email_details['body'])
            body_text.config(state="disabled")
            body_text.pack(fill="both", expand=True, padx=10, pady=10)

            # Pack scrollbar và canvas
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        except Exception as e:
            logger.error(f"Lỗi khi mở cửa sổ chi tiết email: {str(e)}")
            messagebox.showerror("Lỗi", "Không thể mở cửa sổ chi tiết email")
