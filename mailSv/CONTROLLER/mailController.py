# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email, User
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel  # Import EmailModel from models.py

class MailController:
    def __init__(self):
        self.session = create_connection()

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        try:
            email_data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            new_email = Email(sender=email_data.sender, recipients=email_data.recipients, cc=email_data.cc, bcc=email_data.bcc, subject=email_data.subject, body=email_data.body, attachments=email_data.attachments)
            self.session.add(new_email)
            self.session.commit()
            logger.info(f"Email đã được gửi thành công từ {sender} đến {recipients}")
            return "Email đã được gửi thành công"
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi gửi email: {e}")
            return f"Lỗi khi gửi email: {e}"

    def fetch_emails(self, email_type):
        emails = []  # Initialize emails variable
        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            if email_type == "inbox":
                emails = self.session.query(Email).filter(Email.recipients.like("%client@example.com%")).all()
            elif email_type == "sent":
                emails = self.session.query(Email).filter_by(sender="client@example.com").all()
            logger.info(f"Truy xuất {len(emails)} email loại {email_type}")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return f"Lỗi khi truy xuất email: {e}"

    def fetch_all_emails(self):
        if self.session is None:
            return []
        try:
            emails = self.session.query(Email).all()
            logger.info(f"Truy xuất {len(emails)} email")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return []

    def fetch_all_users(self):
        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            users = self.session.query(User).all()
            logger.info(f"Truy xuất {len(users)} người dùng")
            return [user.username for user in users]
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất người dùng: {e}")
            return f"Lỗi khi truy xuất người dùng: {e}"

    def fetch_emails_by_user(self, username, email_type="inbox"):
        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            if email_type == "inbox":
                emails = self.session.query(Email).filter(
                    (Email.recipients.like(f"%{username}%")) |
                    (Email.cc.like(f"%{username}%")) |
                    (Email.bcc.like(f"%{username}%"))
                ).all()
            elif email_type == "sent":
                emails = self.session.query(Email).filter_by(sender=username).all()
            logger.info(f"Truy xuất {len(emails)} email loại {email_type} của người dùng {username}")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return f"Lỗi khi truy xuất email: {e}"

    def search_emails(self, query):
        if self.session is None:
            return []
        try:
            emails = self.session.query(Email).filter(
                (Email.subject.like(f"%{query}%")) |
                (Email.body.like(f"%{query}%"))
            ).all()
            logger.info(f"Tìm kiếm {len(emails)} email với từ khóa {query}")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi tìm kiếm email: {e}")
            return []
