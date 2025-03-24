import json
from loguru import logger
from pydantic import ValidationError
from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
from MODEL.models import EmailModel  # Import EmailModel from models.py

class MailClientProtocol(LineReceiver):
    def __init__(self, controller):
        self.controller = controller

    def connectionMade(self):
        self.sendLine(self.controller.message.encode('utf-8'))

    def lineReceived(self, line):
        response = line.decode('utf-8')
        self.controller.handle_response(response)
        self.transport.loseConnection()

class MailController:
    def __init__(self, user_id):
        self.user_id = user_id

    def send_request(self, message):
        self.message = message
        factory = protocol.ClientFactory()
        factory.protocol = lambda: MailClientProtocol(self)
        reactor.connectTCP('localhost', 65432, factory)

    def handle_response(self, response):
        logger.info(f"Phản hồi từ server: {response}")
        self.view.handle_server_response(response)

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        try:
            email_data = EmailModel(
                sender=sender, 
                recipients=recipients, 
                cc=cc, 
                bcc=bcc, 
                subject=subject, 
                body=body, 
                attachments=attachments
            )
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

        message = f"SEND_EMAIL|{email_data.sender}|{email_data.recipients}|{email_data.cc}|{email_data.bcc}|{email_data.subject}|{email_data.body}|{email_data.attachments}"
        logger.info(f"Gửi yêu cầu gửi email: {message}")
        self.send_request(message)

    def fetch_emails(self, folder):
        request = f"FETCH_EMAILS|{self.user_id}|{folder}"
        logger.info(f"Gửi yêu cầu truy xuất email: {request}")
        self.send_request(request)

    def fetch_all_emails(self):
        request = "FETCH_ALL_EMAILS"
        logger.info(f"Gửi yêu cầu truy xuất tất cả email: {request}")
        self.send_request(request)
