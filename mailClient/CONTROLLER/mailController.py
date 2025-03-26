import socket
import json
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel  # Import EmailModel từ models.py

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
                s.connect(('localhost', 65432))
                s.sendall(request.encode())
                response = s.recv(4096)
                return response.decode()
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
            email_data (EmailModel): Dữ liệu email cần gửi.

        Returns:
            str: Phản hồi từ server.
        """
        try:
            email_data = EmailModel(**email_data)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

        message = f"SEND_EMAIL|{email_data.sender}|{email_data.recipients}|{email_data.cc}|{email_data.bcc}|{email_data.subject}|{email_data.body}|{email_data.attachments}"
        logger.info(f"Gửi yêu cầu gửi email: {message}")
        response = self.send_request(message)

        if not response:
            return "Không thể gửi email. Vui lòng thử lại sau."

        return response

    def fetch_emails(self, folder):
        """
        Truy xuất email từ server theo thư mục.

        Args:
            folder (str): Tên thư mục (inbox, sent, ...).

        Returns:
            list: Danh sách email.
        """
        request = f"FETCH_EMAILS|{self.user_id}|{folder}"
        logger.info(f"Gửi yêu cầu truy xuất email: {request}")
        response = self.send_request(request)
        if not response:
            logger.error("Không nhận được phản hồi từ server")
            return []
        try:
            emails = self.parse_response(response)
            logger.info(f"Truy xuất email thành công: {emails}")
            return emails
        except json.JSONDecodeError as e:
            logger.error(f"Lỗi khi phân tích cú pháp email: {e}")
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
