# khắc phục đường dẫn không chính xác
import sys
import os

from CONTROLLER.emailController import EmailController
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email, User
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel  # Import EmailModel from models.py
from CONTROLLER.fetchMailController import FetchMailController
from CONTROLLER.sendMailController import SendMailController
from CONTROLLER.searchMailController import SearchMailController
import json
from functools import wraps
import time

# Thêm decorator để giới hạn retry và log
def retry_with_limit(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = 0
            error_msg = None
            while retry_count < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retry_count += 1
                    error_msg = str(e)
                    if retry_count < max_retries:
                        logger.warning(f"Lần thử {retry_count}/{max_retries} thất bại: {e}")
                        time.sleep(delay)
            logger.error(f"Đã thử {max_retries} lần không thành công: {error_msg}")
            return {"success": False, "message": f"Thất bại sau {max_retries} lần thử"}
        return wrapper
    return decorator

class MailController:
    def __init__(self):
        self.fetch_mail_controller = FetchMailController()
        self.send_mail_controller = SendMailController()
        self.search_mail_controller = SearchMailController()
        self._error_count = {}  # Đếm số lần lỗi

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        return self.send_mail_controller.send_email(sender, recipients, cc, bcc, subject, body, attachments)

    def fetch_emails(self, email_type):
        return self.fetch_mail_controller.fetch_emails(email_type)

    def fetch_all_emails(self):
        return self.fetch_mail_controller.fetch_all_emails()

    def fetch_all_users(self):
        return self.fetch_mail_controller.fetch_all_users()

    def fetch_emails_by_user(self, username, email_type="inbox"):
        return self.fetch_mail_controller.fetch_emails_by_user(username, email_type)

    def search_emails(self, query):
        return self.search_mail_controller.search_emails(query)

    def fetch_email_details(self, email_id):
        return self.fetch_mail_controller.fetch_email_details(email_id)

    def delete_email(self, email_id: int, user_id: str) -> dict:
        """
        Xóa email của user được chỉ định.

        Args:
            email_id (int): ID của email cần xóa.
            user_id (str): ID của người dùng.

        Returns:
            dict: Kết quả xóa email.
        """
        try:
            email_controller = EmailController()
            result = email_controller.delete_email(email_id, user_id)
            return result
        except Exception as e:
            logger.error(f"Lỗi khi gọi EmailController để xóa email: {e}")
            return {"success": False, "message": "Lỗi không xác định khi xóa email"}

    def send_request(self, request: str) -> str:
        """Gửi request với connection pooling"""
        import socket
        from contextlib import closing

        try:
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
                s.settimeout(5)  # Giảm timeout xuống 5 giây
                s.connect(('localhost', 65432))
                s.sendall(request.encode())
                
                # Thêm keepalive
                s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                response = s.recv(4096)
                
                if not response:
                    return json.dumps({"success": False, "message": "Không nhận được phản hồi"})
                    
                return response.decode()
                
        except Exception as e:
            error_type = type(e).__name__
            if self._error_count.get(error_type, 0) < 3:
                self._error_count[error_type] = self._error_count.get(error_type, 0) + 1
                logger.error(f"{error_type}: {str(e)}")
            return json.dumps({"success": False, "message": str(e)})
