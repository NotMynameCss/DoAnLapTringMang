import json
import datetime
from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
from pydantic import ValidationError
from MODEL.models import EmailModel, RegisterModel, LoginModel
from CONTROLLER.mainController import MainController
from CONTROLLER.mailController import MailController
from utils.logger import get_logger, get_twisted_logger

logger = get_logger()
twisted_logger = get_twisted_logger()

# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

class MailServerProtocol(LineReceiver):
    def __init__(self, main_controller, mail_controller):
        self.main_controller = main_controller
        self.mail_controller = mail_controller

    def lineReceived(self, line):
        message = line.decode('utf-8')
        logger.info(f"Nhận tin nhắn: {message}")
        twisted_logger.info(f"Nhận tin nhắn: {message}")

        try:
            response = self.handle_message(message)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            twisted_logger.error(f"Unexpected error: {e}")
            response = f"Unexpected error: {e}"

        self.sendLine(response.encode('utf-8'))
        logger.info(f"Phản hồi gửi đến client: {response}")
        twisted_logger.info(f"Phản hồi gửi đến client: {response}")

    def handle_message(self, message):
        if message.startswith("REGISTER"):
            return self.handle_register(message)
        elif message.startswith("LOGIN"):
            return self.handle_login(message)
        elif message.startswith("SEND_EMAIL"):
            return self.handle_send_email(message)
        elif message.startswith("FETCH_EMAILS"):
            return self.handle_fetch_emails(message)
        elif message.startswith("FETCH_ALL_EMAILS"):
            return self.handle_fetch_all_emails()
        elif message.startswith("FETCH_ALL_USERS"):
            return self.handle_fetch_all_users()
        elif message.startswith("REFRESH_EMAILS"):
            return self.handle_refresh_emails(message)
        else:
            return "Lệnh không xác định"

    def handle_register(self, message):
        _, username, password = message.split()
        try:
            data = RegisterModel(username=username, password=password)
            return self.main_controller.handle_register(data.username, data.password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            twisted_logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

    def handle_login(self, message):
        _, username, password = message.split()
        try:
            data = LoginModel(username=username, password=password)
            return self.main_controller.handle_login(data.username, data.password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            twisted_logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

    def handle_send_email(self, message):
        _, sender, recipients, cc, bcc, subject, body, attachments = message.split('|')
        try:
            data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
            return self.mail_controller.send_email(data.sender, data.recipients, data.cc, data.bcc, data.subject, data.body, data.attachments)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            twisted_logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

    def handle_fetch_emails(self, message):
        _, username, email_type = message.split('|')
        emails = self.mail_controller.fetch_emails_by_user(username, email_type)
        return json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"

    def handle_fetch_all_emails(self):
        emails = self.mail_controller.fetch_all_emails()
        return json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"

    def handle_fetch_all_users(self):
        return self.mail_controller.fetch_all_users()

    def handle_refresh_emails(self, message):
        _, username = message.split('|')
        emails = self.mail_controller.fetch_emails_by_user(username)
        return json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"

class MailServerFactory(protocol.Factory):
    def __init__(self, main_controller, mail_controller):
        self.main_controller = main_controller
        self.mail_controller = mail_controller

    def buildProtocol(self, addr):
        return MailServerProtocol(self.main_controller, self.mail_controller)

def start_server(main_controller, mail_controller):
    factory = MailServerFactory(main_controller, mail_controller)
    reactor.listenTCP(65432, factory)
    logger.info("Máy chủ đang lắng nghe trên cổng 65432")
    twisted_logger.info("Máy chủ đang lắng nghe trên cổng 65432")
    # Do not call reactor.run() here, it will be called in the main thread

if __name__ == "__main__":
    main_controller = MainController(None)
    mail_controller = MailController()
    start_server(main_controller, mail_controller)
    reactor.run()
