# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, Dict, Any
from MODEL.dbconnector import create_connection, Email, User
from loguru import logger

class FetchMailController:
    """Controller truy xuất email và người dùng."""

    def __init__(self):
        """Khởi tạo session database."""
        self.session = create_connection()

    def fetch_emails(self, email_type):
        """Lấy danh sách email theo loại (inbox/sent)."""
        if self.session is None:
            logger.error("Lỗi kết nối đến database")
            return []
        try:
            if email_type == "inbox":
                emails = self.session.query(Email).filter(Email.recipients.like("%client@example.com%")).all()
            elif email_type == "sent":
                emails = self.session.query(Email).filter_by(sender="client@example.com").all()
            else:
                emails = []
            logger.info(f"Truy xuất {len(emails)} email loại {email_type}")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return []

    def fetch_all_emails(self):
        """Lấy tất cả email."""
        if self.session is None:
            logger.error("Lỗi kết nối đến database")
            return []
        try:
            emails = self.session.query(Email).all()
            logger.info(f"Truy xuất {len(emails)} email")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return []

    def fetch_all_users(self):
        """Lấy danh sách tất cả người dùng."""
        if self.session is None:
            logger.error("Lỗi kết nối đến database")
            return []
        try:
            users = self.session.query(User).all()
            logger.info(f"Truy xuất {len(users)} người dùng")
            return [user.username for user in users]
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất người dùng: {e}")
            return []

    def fetch_emails_by_user(self, username, email_type="inbox"):
        """Lấy email theo user và loại (inbox/sent)."""
        if self.session is None:
            logger.error("Lỗi kết nối đến database")
            return []
        try:
            if email_type == "inbox":
                emails = self.session.query(Email).filter(
                    (Email.recipients.like(f"%{username}%")) |
                    (Email.cc.like(f"%{username}%")) |
                    (Email.bcc.like(f"%{username}%"))
                ).all()
            elif email_type == "sent":
                emails = self.session.query(Email).filter_by(sender=username).all()
            else:
                emails = []
            logger.info(f"Truy xuất {len(emails)} email loại {email_type} của người dùng {username}")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return []

    def fetch_email_details(self, email_id: int) -> Optional[Dict[str, Any]]:
        """Lấy chi tiết email từ database."""
        if self.session is None:
            logger.error("Lỗi kết nối đến database")
            return None
        try:
            if not email_id:
                logger.error("Email ID không được để trống")
                return None
            try:
                email_id = int(email_id)
            except (TypeError, ValueError):
                logger.error(f"Email ID không hợp lệ: {email_id}")
                return None
            logger.debug(f"Đang truy xuất email với ID: {email_id}")
            email = self.session.query(Email).get(email_id)
            if email:
                logger.info(f"Tìm thấy email với ID {email_id}")
                return {
                    'id': email.id,
                    'sender': email.sender,
                    'recipients': email.recipients,
                    'cc': email.cc,
                    'bcc': email.bcc,
                    'subject': email.subject,
                    'body': email.body,
                    'attachments': email.attachments,
                    'timestamp': email.timestamp.strftime('%Y-%m-%d %H:%M:%S') if email.timestamp else None
                }
            else:
                logger.warning(f"Không tìm thấy email với ID: {email_id}")
                return None
        except SQLAlchemyError as e:
            logger.error(f"Lỗi database khi truy xuất email {email_id}: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Lỗi không xác định khi truy xuất email {email_id}: {str(e)}")
            return None
