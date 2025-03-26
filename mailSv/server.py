import datetime
import socket
import threading
import json
from loguru import logger
from pydantic import ValidationError
from concurrent.futures import ThreadPoolExecutor
from MODEL.models import EmailModel, RegisterModel, LoginModel  # Import models from models.py
from CONTROLLER.mainController import MainController
from CONTROLLER.mailController import MailController

# Configure loguru
logger.add("mail_server.log", rotation="1 MB", retention="10 days", level="INFO")

# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

def receive_with_timeout(client_socket, timeout=30):
    client_socket.settimeout(timeout)
    try:
        message = client_socket.recv(1024).decode('utf-8')
        return message
    except socket.timeout:
        return None

def is_valid_message_format(message):
    # Implement your message format validation logic here
    return True

def send_error_response(client_socket, error_message):
    response = json.dumps({"success": False, "message": error_message})
    client_socket.send(response.encode('utf-8'))

def send_response_with_ack(client_socket, response):
    client_socket.send(response.encode('utf-8'))
    ack = client_socket.recv(1024).decode('utf-8')
    if ack != "ACK":
        logger.warning("Client did not acknowledge the response")

def process_message(message, main_controller, mail_controller):
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
    return response

def handle_delete_email(mail_controller, email_id, user_id):
    """
    Xử lý xóa email với timeout và error handling.
    """
    try:
        logger.info(f"Processing DELETE_EMAIL request: id={email_id}, user={user_id}")

        # Thêm timeout cho database operation
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(mail_controller.delete_email, int(email_id), user_id)
            try:
                result = future.result(timeout=10)
            except TimeoutError:
                logger.error("Timeout khi xử lý xóa email")
                return json.dumps({
                    "success": False,
                    "message": "Timeout khi xử lý xóa email"
                })

        # Log kết quả
        if result.get("success"):
            logger.info(f"Xóa email thành công: {result}")
        else:
            logger.warning(f"Lỗi khi xóa email: {result.get('message')}")
        return json.dumps(result)

    except Exception as e:
        logger.error(f"Lỗi khi xử lý DELETE_EMAIL: {e}")
        return json.dumps({
            "success": False,
            "message": "Lỗi không xác định khi xử lý DELETE_EMAIL {e}"
        })

def handle_client(client_socket, main_controller, mail_controller):
    try:
        client_socket.settimeout(30)  # Set timeout 30 seconds
        
        while True:
            try:
                message = receive_with_timeout(client_socket)
                if not message:
                    break

                # Validate message format
                if not is_valid_message_format(message):
                    send_error_response(client_socket, "Invalid message format")
                    continue

                # Process message and send response with acknowledgment
                response = process_message(message, main_controller, mail_controller)
                send_response_with_ack(client_socket, response)

            except socket.timeout:
                logger.warning("Client connection timeout")
                break
            except ConnectionError as e:
                logger.error(f"Connection error: {e}")
                break
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                send_error_response(client_socket, "Internal server error")
                continue

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
