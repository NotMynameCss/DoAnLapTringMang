# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel

class SendMailController:
    """Controller gửi email."""

    def __init__(self):
        """Khởi tạo session database."""
        self.session = create_connection()

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        """Gửi email mới vào database."""
        try:
            email_data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return {"success": False, "message": f"Lỗi xác thực dữ liệu: {e}"}

        if self.session is None:
            logger.error("Lỗi kết nối đến database")
            return {"success": False, "message": "Lỗi kết nối đến database"}
        try:
            new_email = Email(
                sender=email_data.sender,
                recipients=email_data.recipients,
                cc=email_data.cc,
                bcc=email_data.bcc,
                subject=email_data.subject,
                body=email_data.body,
                attachments=email_data.attachments
            )
            self.session.add(new_email)
            self.session.commit()
            logger.info(f"Email đã được gửi thành công từ {sender} đến {recipients}")
            return {"success": True, "message": "Email đã được gửi thành công"}
        except SQLAlchemyError as e:
            self.session.rollback()
            logger.error(f"Lỗi khi gửi email: {e}")
            return {"success": False, "message": f"Lỗi khi gửi email: {e}"}
