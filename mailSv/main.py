# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
import json
import socket
import threading
from VIEW.mainView import MainView
from CONTROLLER.mainController import MainController
from CONTROLLER.mailController import MailController
import datetime
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel, RegisterModel, LoginModel  # Import models from models.py

# Configure loguru
logger.add("mail_server.log", rotation="1 MB", retention="10 days", level="INFO")

# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

def handle_client(client_socket, main_controller, mail_controller):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            logger.info(f"Nhận tin nhắn: {message}")

            if message.startswith("REGISTER"):
                _, username, password = message.split()
                try:
                    data = RegisterModel(username=username, password=password)
                    response = main_controller.handle_register(data.username, data.password)
                except ValidationError as e:
                    logger.error(f"Lỗi xác thực dữ liệu: {e}")
                    response = f"Lỗi xác thực dữ liệu: {e}"
            elif message.startswith("LOGIN"):
                _, username, password = message.split()
                try:
                    data = LoginModel(username=username, password=password)
                    response = main_controller.handle_login(data.username, data.password)
                except ValidationError as e:
                    logger.error(f"Lỗi xác thực dữ liệu: {e}")
                    response = f"Lỗi xác thực dữ liệu: {e}"
            elif message.startswith("SEND_EMAIL"):
                _, sender, recipients, cc, bcc, subject, body, attachments = message.split('|')
                try:
                    data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
                    response = mail_controller.send_email(data.sender, data.recipients, data.cc, data.bcc, data.subject, data.body, data.attachments)
                except ValidationError as e:
                    logger.error(f"Lỗi xác thực dữ liệu: {e}")
                    response = f"Lỗi xác thực dữ liệu: {e}"
            elif message.startswith("FETCH_EMAILS"):
                _, username, email_type = message.split('|')
                emails = mail_controller.fetch_emails_by_user(username, email_type)
                response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
            elif message.startswith("FETCH_ALL_EMAILS"):
                if '|' in message:
                    _, username = message.split('|')
                    emails = mail_controller.fetch_emails_by_user(username)
                else:
                    emails = mail_controller.fetch_all_emails()
                response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
            elif message.startswith("FETCH_ALL_USERS"):
                response = mail_controller.fetch_all_users()
            elif message.startswith("REFRESH_EMAILS"):
                _, username = message.split('|')
                emails = mail_controller.fetch_emails_by_user(username)
                response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
            else:
                response = "Lệnh không xác định"

            client_socket.send(response.encode('utf-8'))
            logger.info(f"Phản hồi gửi đến client: {response}")
    except Exception as e:
        logger.error(f"Lỗi: {e}")
    finally:
        client_socket.close()

def start_server(main_controller, mail_controller):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 65432))
    server.listen(5)
    logger.info("Máy chủ đang lắng nghe trên cổng 65432")

    try:
        while True:
            client_socket, addr = server.accept()
            logger.info(f"Chấp nhận kết nối từ {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, main_controller, mail_controller))
            client_handler.start()
    except KeyboardInterrupt:
        logger.info("Máy chủ đang tắt")
    finally:
        server.close()

if __name__ == "__main__":
    root = tk.Tk()
    main_controller = MainController(MainView(root))
    mail_controller = MailController()

    server_thread = threading.Thread(target=start_server, args=(main_controller, mail_controller))
    server_thread.start()

    root.mainloop()
