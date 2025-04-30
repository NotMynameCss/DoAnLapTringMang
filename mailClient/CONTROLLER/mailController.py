import socket
import json
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel  # Import EmailModel từ models.py
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from client_network_config import MAILSV_HOST, MAILSV_PORT


class MailController:
    """
    Controller quản lý các hoạt động liên quan đến email như gửi email, truy xuất email.
    """

    def __init__(self, user_id):
        """
        Khởi tạo MailController với user_id.
        """
        self.user_id = user_id

    def send_request(self, request):
        """
        Gửi yêu cầu đến server qua giao thức TCP/IP.

        Args:
            request (str): Yêu cầu cần gửi.

        Returns:
            str: Phản hồi từ server.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(10)  # Thêm timeout để tránh treo kết nối
                s.connect((MAILSV_HOST, MAILSV_PORT))
                s.sendall(request.encode())

                response = s.recv(4096)  # Nhận phản hồi từ server

                # Gửi ACK để xác nhận giúp tránh trường hợp làm giảm tốc độc xử lý TCP/IP. 
                # VD: server tăng retransmission nếu không nhận được ACK
                s.sendall("ACK".encode())

                # Đảm bảo phản hồi là string
                return response.decode('utf-8')
        except ConnectionRefusedError as e:
            logger.error(f"Lỗi kết nối đến server: {e}")
            return "Lỗi kết nối đến server."
        except socket.timeout as e:
            logger.error(f"Timeout khi kết nối đến server: {e}")
            return "Timeout khi kết nối đến server."
        except socket.error as e:
            logger.error(f"Lỗi socket: {e}")
            return "Lỗi socket."

    def send_email(self, email_data):
        """
        Gửi email với thông tin được cung cấp.

        Args:
            email_data (dict): Dữ liệu email cần gửi.

        Returns:
            str: Phản hồi từ server.
        """
        try:
            email_data = EmailModel(**email_data)  # Validate dữ liệu bằng Pydantic
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

        message = f"SEND_EMAIL|{email_data.sender}|{email_data.recipients}|{email_data.cc}|{email_data.bcc}|{email_data.subject}|{email_data.body}|{email_data.attachments}"
        logger.info(f"Gửi yêu cầu gửi email: {message}")
        response = self.send_request(message)

        if not response:
            return "Không thể gửi email. Vui lòng thử lại sau."

        # Parse response JSON, trả về message rõ ràng
        try:
            result = json.loads(response)
            if isinstance(result, dict) and result.get("success"):
                return result.get("message", "Email đã được gửi thành công")
            elif isinstance(result, dict):
                return result.get("message", "Gửi email thất bại")
            else:
                logger.error(f"Phản hồi không hợp lệ: {response}")
                return "Phản hồi không hợp lệ từ server."
        except Exception as e:
            logger.error(f"Lỗi khi parse phản hồi gửi email: {e} | response={response}")
            return "Lỗi khi xử lý phản hồi từ server."

    def fetch_emails(self, folder):
        """
        Truy xuất email từ server theo thư mục.

        Args:
            folder (str): Tên thư mục (inbox, sent, ...).

        Returns:
            list: Danh sách email.
        """
        try:
            request = f"FETCH_EMAILS|{self.user_id}|{folder}"
            logger.info(f"Gửi yêu cầu truy xuất email: {request}")
            response = self.send_request(request)
            
            if not response:
                logger.error("Không nhận được phản hồi từ server.")
                return []

            emails = self.parse_response(response)
            logger.info(f"Truy xuất email thành công: {len(emails)} email.")
            return emails

        except json.JSONDecodeError as e:
            logger.error(f"Lỗi phân tích cú pháp JSON từ phản hồi: {e}")
            return []
        except Exception as e:
            logger.error(f"Lỗi không xác định khi truy xuất email: {e}")
            return []

    def fetch_all_emails(self):
        """
        Truy xuất tất cả email từ server.

        Returns:
            list: Danh sách tất cả email.
        """
        request = "FETCH_ALL_EMAILS"
        logger.info(f"Gửi yêu cầu truy xuất tất cả email: {request}")
        response = self.send_request(request)
        if not response:
            logger.error("Không nhận được phản hồi từ server")
            return []
        try:
            emails = json.loads(response) if response else []
            logger.info(f"Truy xuất tất cả email thành công: {emails}")
            return emails
        except json.JSONDecodeError as e:
            logger.error(f"Lỗi khi phân tích cú pháp email: {e}")
            return []

    def parse_response(self, response):
        """
        Phân tích phản hồi từ server.

        Args:
            response (str): Phản hồi từ server.

        Returns:
            list: Danh sách email.
        """
        return json.loads(response)

    def delete_email(self, email_id: int) -> dict:
        """
        Gửi yêu cầu xóa email đến server và làm mới danh sách email.

        Args:
            email_id (int): ID của email cần xóa.

        Returns:
            dict: Kết quả từ server.
        """
        try:
            # Validate email_id
            if not isinstance(email_id, int) or email_id <= 0:
                logger.error(f"Email ID không hợp lệ: {email_id}")
                return {"success": False, "message": "Email ID không hợp lệ"}

            # Format request
            request = f"DELETE_EMAIL|{email_id}|{self.user_id}"
            logger.info(f"Gửi yêu cầu xóa email: {request}")

            # Gửi request đến server
            response = self.send_request(request)
            if not response:
                raise ValueError("Không nhận được phản hồi từ server")

            # Parse response
            result = json.loads(response)
            if result.get("success"):
                logger.info(f"Xóa email thành công: ID={email_id}")
                # Làm mới danh sách email sau khi xóa thành công
                self.refresh_emails()
            else:
                logger.warning(f"Lỗi khi xóa email: {result.get('message')}")

            return result

        except json.JSONDecodeError as e:
            logger.error(f"Lỗi parse JSON từ response: {e}")
            return {"success": False, "message": "Phản hồi từ server không hợp lệ"}
        except Exception as e:
            logger.error(f"Lỗi không xác định khi xóa email: {e}")
            return {"success": False, "message": str(e)}

    def refresh_emails(self):
        """
        Làm mới danh sách email từ server.
        """
        try:
            logger.info("Đang làm mới danh sách email từ server...")
            emails = self.fetch_emails("inbox")
            logger.info(f"Làm mới thành công: {len(emails)} email được tải.")
        except Exception as e:
            logger.error(f"Lỗi khi làm mới danh sách email: {e}")
