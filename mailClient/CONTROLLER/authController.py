import socket
from loguru import logger
from pydantic import ValidationError
from MODEL.models import UserModel, RegisterModel, LoginModel  # Import models from models.py

class AuthController:
    def __init__(self, view):
        self.view = view

    def send_request(self, message):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 65432))
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            client_socket.close()
            logger.info(f"Phản hồi từ server: {response}")
            return response
        except Exception as e:
            logger.error(f"Lỗi kết nối đến server: {e}")
            return f"Lỗi kết nối đến server: {e}"

    def login(self, username, password):
        try:
            user_data = LoginModel(username=username, password=password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"
        message = f"LOGIN {user_data.username} {user_data.password}"
        logger.info(f"Gửi yêu cầu đăng nhập: {message}")
        response = self.send_request(message)
        return response

    def register(self, username, password):
        try:
            user_data = RegisterModel(username=username, password=password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"
        message = f"REGISTER {user_data.username} {user_data.password}"
        logger.info(f"Gửi yêu cầu đăng ký: {message}")
        response = self.send_request(message)
        return response
