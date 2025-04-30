"""Module MailController: Quản lý các thao tác email, user, networking cho mail server."""

import os
import sys
import json
import time
from functools import wraps
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from contextlib import closing
from network_config import SERVER_HOST, SERVER_PORT  # Sử dụng cấu hình chung

from CONTROLLER.emailController import EmailController
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MODEL.dbconnector import create_connection, Email, User
from CONTROLLER.fetchMailController import FetchMailController
from CONTROLLER.sendMailController import SendMailController
from CONTROLLER.searchMailController import SearchMailController

def retry_with_limit(max_retries=3, delay=1):
    """Decorator để retry với giới hạn số lần và log lỗi."""
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
    """MailController: Quản lý các thao tác email, user, networking."""

    def __init__(self):
        """Khởi tạo các controller con."""
        self.fetch_mail_controller = FetchMailController()
        self.send_mail_controller = SendMailController()
        self.search_mail_controller = SearchMailController()
        self._error_count = {}

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        """Gửi email mới."""
        return self.send_mail_controller.send_email(sender, recipients, cc, bcc, subject, body, attachments)

    def fetch_emails(self, email_type):
        """Lấy danh sách email theo loại."""
        result = self.fetch_mail_controller.fetch_emails(email_type)
        if isinstance(result, str):
            logger.error(f"Lỗi khi fetch_emails: {result}")
            return []
        return result

    def fetch_all_emails(self):
        """Lấy tất cả email."""
        result = self.fetch_mail_controller.fetch_all_emails()
        if isinstance(result, str):
            logger.error(f"Lỗi khi fetch_all_emails: {result}")
            return []
        return result

    def fetch_all_users(self):
        """Lấy danh sách tất cả người dùng."""
        result = self.fetch_mail_controller.fetch_all_users()
        if isinstance(result, str):
            logger.error(f"Lỗi khi fetch_all_users: {result}")
            return []
        return result

    def fetch_emails_by_user(self, username, email_type="inbox"):
        """Lấy email theo user và loại."""
        result = self.fetch_mail_controller.fetch_emails_by_user(username, email_type)
        if isinstance(result, str):
            logger.error(f"Lỗi khi fetch_emails_by_user: {result}")
            return []
        return result

    def search_emails(self, query):
        """Tìm kiếm email theo từ khóa."""
        return self.search_mail_controller.search_emails(query)

    def fetch_email_details(self, email_id):
        """Lấy chi tiết email."""
        return self.fetch_mail_controller.fetch_email_details(email_id)

    def delete_email(self, email_id: int, user_id: str) -> dict:
        """Xóa email của user được chỉ định."""
        try:
            email_controller = EmailController()
            result = email_controller.delete_email(email_id, user_id)
            if not isinstance(result, dict):
                logger.error(f"Kết quả xóa email không hợp lệ: {result}")
                return {"success": False, "message": "Kết quả xóa email không hợp lệ"}
            return result
        except SQLAlchemyError as e:
            logger.error(f"Lỗi SQLAlchemy khi xóa email: {e}")
            return {"success": False, "message": "Lỗi database khi xóa email"}
        except Exception as e:
            logger.error(f"Lỗi khi gọi EmailController để xóa email: {e}")
            return {"success": False, "message": "Lỗi không xác định khi xóa email"}

    def send_request(self, request: str) -> str:
        """Gửi request TCP tới server (dùng connection pooling)."""
        import socket
        

        try:
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
                s.settimeout(5)
                s.connect((SERVER_HOST, SERVER_PORT))
                s.sendall(request.encode())
                s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                response = s.recv(4096)
                if not response:
                    logger.error("Không nhận được phản hồi từ server")
                    return json.dumps({"success": False, "message": "Không nhận được phản hồi"})
                return response.decode()
        except (socket.timeout, ConnectionRefusedError) as e:
            logger.error(f"Lỗi kết nối TCP: {e}")
            return json.dumps({"success": False, "message": f"Lỗi kết nối TCP: {e}"})
        except Exception as e:
            error_type = type(e).__name__
            if self._error_count.get(error_type, 0) < 3:
                self._error_count[error_type] = self._error_count.get(error_type, 0) + 1
                logger.error(f"{error_type}: {str(e)}")
            return json.dumps({"success": False, "message": str(e)})
