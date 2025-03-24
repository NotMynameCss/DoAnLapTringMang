# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, Dict, Any
from MODEL.dbconnector import create_connection, Email, User, DBConnection
from loguru import logger

class FetchMailController:
    def __init__(self):
        self.session = create_connection()

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

    def fetch_email_details(self, email_id: int) -> Optional[Dict[str, Any]]:
        """
        Lấy chi tiết email từ database
        
        Args:
            email_id: ID của email cần lấy thông tin
            
        Returns:
            Dict chứa thông tin chi tiết email hoặc None nếu không tìm thấy
        """
        try:
            if not email_id:
                logger.error("Email ID không được để trống")
                return None
                
            # Đảm bảo email_id là số nguyên
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
