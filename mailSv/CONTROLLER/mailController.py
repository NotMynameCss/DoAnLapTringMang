# khắc phục đường dẫn không chính xác
import sys
import os
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

class MailController:
    def __init__(self):
        self.fetch_mail_controller = FetchMailController()
        self.send_mail_controller = SendMailController()
        self.search_mail_controller = SearchMailController()

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
        """
        # Loại bỏ toàn bộ nội dung phương thức delete_email

    def send_request(self, request: str) -> str:
        """
        Gửi yêu cầu đến server qua giao thức TCP/IP.

        Args:
            request (str): Yêu cầu cần gửi.

        Returns:
            str: Phản hồi từ server.
        """
        import socket
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(10)  # Thêm timeout để tránh treo kết nối
                s.connect(('localhost', 65432))
                s.sendall(request.encode())
                response = s.recv(4096)
                if not response:
                    logger.error("Phản hồi từ server rỗng")
                    return json.dumps({"success": False, "message": "Phản hồi từ server rỗng"})
                return response.decode()
        except ConnectionRefusedError as e:
            logger.error(f"Lỗi kết nối đến server: {e}")
            return json.dumps({"success": False, "message": "Lỗi kết nối đến server"})
        except socket.timeout as e:
            logger.error(f"Timeout khi kết nối đến server: {e}")
            return json.dumps({"success": False, "message": "Timeout khi kết nối đến server"})
        except socket.error as e:
            logger.error(f"Lỗi socket: {e}")
            return json.dumps({"success": False, "message": "Lỗi socket"})
