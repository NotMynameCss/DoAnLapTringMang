import socket
from loguru import logger
from pydantic import ValidationError
from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
from MODEL.models import UserModel, RegisterModel, LoginModel  # Import models from models.py

class AuthClientProtocol(LineReceiver):
    def __init__(self, controller):
        self.controller = controller

    def connectionMade(self):
        self.sendLine(self.controller.message.encode('utf-8'))

    def lineReceived(self, line):
        response = line.decode('utf-8')
        self.controller.handle_response(response)
        self.transport.loseConnection()

class AuthController:
    def __init__(self, view):
        self.view = view

    def send_request(self, message):
        self.message = message
        factory = protocol.ClientFactory()
        factory.protocol = lambda: AuthClientProtocol(self)
        reactor.connectTCP('localhost', 65432, factory)

    def handle_response(self, response):
        logger.info(f"Phản hồi từ server: {response}")
        self.view.handle_server_response(response)

    def login(self, username, password):
        try:
            user_data = LoginModel(username=username, password=password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"
        message = f"LOGIN {user_data.username} {user_data.password}"
        logger.info(f"Gửi yêu cầu đăng nhập: {message}")
        self.send_request(message)

    def register(self, username, password):
        try:
            user_data = RegisterModel(username=username, password=password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"
        message = f"REGISTER {user_data.username} {user_data.password}"
        logger.info(f"Gửi yêu cầu đăng ký: {message}")
        self.send_request(message)
