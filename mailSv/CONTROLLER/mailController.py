# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MODEL.dbconnector import create_connection, create_email_table
from mysql.connector import Error

class MailController:
    def __init__(self):
        self.connection = create_connection()
        create_email_table(self.connection)

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO emails (sender, recipients, cc, bcc, subject, body, attachments)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (sender, recipients, cc, bcc, subject, body, attachments))
            self.connection.commit()
            return "Email đã được gửi thành công"
        except Error as e:
            return f"Lỗi khi gửi email: {e}"

    def fetch_emails(self, email_type):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor()
            if email_type == "inbox":
                cursor.execute("SELECT * FROM emails WHERE recipients LIKE %s", ("%client@example.com%",))
            elif email_type == "sent":
                cursor.execute("SELECT * FROM emails WHERE sender = %s", ("client@example.com",))
            emails = cursor.fetchall()
            return "\n".join([f"From: {email[1]}, To: {email[2]}, Subject: {email[5]}" for email in emails])
        except Error as e:
            return f"Lỗi khi truy xuất email: {e}"

    def fetch_all_emails(self):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM emails")
            emails = cursor.fetchall()
            return emails
        except Error as e:
            return f"Lỗi khi truy xuất email: {e}"

    def fetch_all_users(self):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT username FROM users")
            users = cursor.fetchall()
            return [user[0] for user in users]
        except Error as e:
            return f"Lỗi khi truy xuất người dùng: {e}"

    def fetch_emails_by_user(self, username):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT * FROM emails 
                WHERE sender = %s OR recipients LIKE %s OR cc LIKE %s OR bcc LIKE %s
            """, (username, f"%{username}%", f"%{username}%", f"%{username}%"))
            emails = cursor.fetchall()
            return emails
        except Error as e:
            return f"Lỗi khi truy xuất email: {e}"

    def refresh_emails(self):
        return self.fetch_all_emails()
