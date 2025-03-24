import json
import datetime
from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
from twisted.logger import Logger, globalLogBeginner, textFileLogObserver
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel, RegisterModel, LoginModel
from CONTROLLER.mainController import MainController
from CONTROLLER.mailController import MailController

# Ensure the logMailSv directory exists
import os
log_dir = os.path.join(os.path.dirname(__file__), 'logMailSv')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure loguru for general server logs
logger.add(os.path.join(log_dir, "log_server.log"), rotation="1 MB", retention="10 days", level="INFO")

# Configure twisted.logger for Twisted-related logs
globalLogBeginner.beginLoggingTo([textFileLogObserver(open(os.path.join(log_dir, "twisted_server.log"), "a"))])
twisted_logger = Logger()

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

        if message.startswith("REGISTER"):
            _, username, password = message.split()
            try:
                data = RegisterModel(username=username, password=password)
                response = self.main_controller.handle_register(data.username, data.password)
            except ValidationError as e:
                logger.error(f"Lỗi xác thực dữ liệu: {e}")
                twisted_logger.error(f"Lỗi xác thực dữ liệu: {e}")
                response = f"Lỗi xác thực dữ liệu: {e}"
        elif message.startswith("LOGIN"):
            _, username, password = message.split()
            try:
                data = LoginModel(username=username, password=password)
                response = self.main_controller.handle_login(data.username, data.password)
            except ValidationError as e:
                logger.error(f"Lỗi xác thực dữ liệu: {e}")
                twisted_logger.error(f"Lỗi xác thực dữ liệu: {e}")
                response = f"Lỗi xác thực dữ liệu: {e}"
        elif message.startswith("SEND_EMAIL"):
            _, sender, recipients, cc, bcc, subject, body, attachments = message.split('|')
            try:
                data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
                response = self.mail_controller.send_email(data.sender, data.recipients, data.cc, data.bcc, data.subject, data.body, data.attachments)
            except ValidationError as e:
                logger.error(f"Lỗi xác thực dữ liệu: {e}")
                twisted_logger.error(f"Lỗi xác thực dữ liệu: {e}")
                response = f"Lỗi xác thực dữ liệu: {e}"
        elif message.startswith("FETCH_EMAILS"):
            _, username, email_type = message.split('|')
            emails = self.mail_controller.fetch_emails_by_user(username, email_type)
            response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
        elif message.startswith("FETCH_ALL_EMAILS"):
            emails = self.mail_controller.fetch_all_emails()
            response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
        elif message.startswith("FETCH_ALL_USERS"):
            response = self.mail_controller.fetch_all_users()
        elif message.startswith("REFRESH_EMAILS"):
            _, username = message.split('|')
            emails = self.mail_controller.fetch_emails_by_user(username)
            response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
        else:
            response = "Lệnh không xác định"

        self.sendLine(response.encode('utf-8'))
        logger.info(f"Phản hồi gửi đến client: {response}")
        twisted_logger.info(f"Phản hồi gửi đến client: {response}")

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
