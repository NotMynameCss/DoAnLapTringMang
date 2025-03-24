# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email
from pydantic import ValidationError
from MODEL.models import EmailModel  # Import EmailModel from models.py
from utils.logger import get_logger

logger = get_logger()

class SendMailController:
    def __init__(self):
        self.session = create_connection()
        if self.session is None:
            logger.error("Failed to create database connection")

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
            self.session.rollback()
            return f"Lỗi khi gửi email: {e}"
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            self.session.rollback()
            return f"Unexpected error: {e}"
