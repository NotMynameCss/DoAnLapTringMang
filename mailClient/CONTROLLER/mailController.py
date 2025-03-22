import socket
import json
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel  # Import EmailModel from models.py

class MailController:
    def __init__(self, user_id):
        self.user_id = user_id

    def send_request(self, request):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', 65432))
                s.sendall(request.encode())
                response = s.recv(4096)
                return response.decode()
        except ConnectionRefusedError as e:
            logger.error(f"Lỗi kết nối đến server: {e}")
            return ""

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        try:
            email_data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"
        message = f"SEND_EMAIL|{email_data.sender}|{email_data.recipients}|{email_data.cc}|{email_data.bcc}|{email_data.subject}|{email_data.body}|{email_data.attachments}"
        logger.info(f"Gửi yêu cầu gửi email: {message}")
        response = self.send_request(message)
        return response

    def fetch_emails(self, folder):
        request = f"FETCH_EMAILS|{self.user_id}|{folder}"
        logger.info(f"Gửi yêu cầu truy xuất email: {request}")
        response = self.send_request(request)
        if not response:
            logger.error("Không nhận được phản hồi từ server")
            return []
        logger.info(f"Phản hồi từ server: {response}")
        emails = self.parse_response(response)
        logger.info(f"Truy xuất email thành công: {emails}")
        return emails

    def fetch_all_emails(self):
        request = f"FETCH_ALL_EMAILS|{self.user_id}"
        logger.info(f"Gửi yêu cầu truy xuất tất cả email: {request}")
        response = self.send_request(request)
        if not response:
            logger.error("Không nhận được phản hồi từ server")
            return []
        try:
            emails = json.loads(response) if response else []
            logger.info(f"Truy xuất tất cả email thành công: {emails}")
        except json.JSONDecodeError as e:
            logger.error(f"Lỗi khi phân tích cú pháp email: {e}")
            emails = []
        return emails

    def parse_response(self, response):
        # Assuming the response is a JSON string of emails
        return json.loads(response)
