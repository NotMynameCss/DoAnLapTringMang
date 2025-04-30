# quản lí các request từ mailClient
import datetime
import socket
import threading
import json
from loguru import logger
from pydantic import ValidationError
from concurrent.futures import ThreadPoolExecutor
from MODEL.models import EmailModel, RegisterModel, LoginModel  # Import models từ models.py
from CONTROLLER.mainController import MainController
from CONTROLLER.mailController import MailController
from network_config import SERVER_HOST, SERVER_PORT

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
    try:
        # Nếu response là dict thì chuyển sang JSON string trước khi gửi
        if isinstance(response, dict):
            response = json.dumps(response, cls=DateTimeEncoder)
        # Nếu response không phải string thì chuyển sang string
        if not isinstance(response, str):
            response = str(response)
        client_socket.send(response.encode('utf-8'))
        ack = client_socket.recv(1024).decode('utf-8')
        if ack != "ACK":
            logger.warning("Client không gửi ACK")
    except socket.timeout:
        logger.error("Timeout while waiting for client ACK")
    except Exception as e:
        logger.error(f"Error in send_response_with_ack: {e}")

def process_message(message, main_controller, mail_controller, client_addr):
    """Xử lý message và log đầy đủ thông tin user, IP, port, action."""
    ip, port = client_addr if client_addr else ("unknown", "unknown")
    user = "unknown"
    action = "unknown"
    try:
        if message.startswith("REGISTER"):
            _, username, password = message.split()
            user = username
            action = "REGISTER"
            logger.info(f"[{action}] user={user} ip={ip}")
            data = RegisterModel(username=username, password=password)
            response = main_controller.handle_register(data.username, data.password)
        elif message.startswith("LOGIN"):
            _, username, password = message.split()
            user = username
            action = "LOGIN"
            logger.info(f"[{action}] user={user} ip={ip}")
            data = LoginModel(username=username, password=password)
            response = main_controller.handle_login(data.username, data.password)
        elif message.startswith("SEND_EMAIL"):
            _, sender, recipients, cc, bcc, subject, body, attachments = message.split('|')
            user = sender
            action = "SEND_EMAIL"
            logger.info(f"[{action}] user={user} ip={ip}")
            data = EmailModel(sender=sender, recipients=recipients, cc=cc, bcc=bcc, subject=subject, body=body, attachments=attachments)
            response = mail_controller.send_email(data.sender, data.recipients, data.cc, data.bcc, data.subject, data.body, data.attachments)
        elif message.startswith("FETCH_EMAILS"):
            _, username, email_type = message.split('|')
            user = username
            action = f"FETCH_EMAILS ({email_type})"
            logger.info(f"[{action}] user={user} ip={ip}")
            emails = mail_controller.fetch_emails_by_user(username, email_type)
            response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
        elif message.startswith("FETCH_ALL_EMAILS"):
            action = "FETCH_ALL_EMAILS"
            logger.info(f"[{action}] user={user} ip={ip}")
            emails = mail_controller.fetch_all_emails()
            response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
        elif message.startswith("FETCH_ALL_USERS"):
            action = "FETCH_ALL_USERS"
            logger.info(f"[{action}] user={user} ip={ip}")
            response = mail_controller.fetch_all_users()
        elif message.startswith("REFRESH_EMAILS"):
            _, username = message.split('|')
            user = username
            action = "REFRESH_EMAILS"
            logger.info(f"[{action}] user={user} ip={ip}")
            emails = mail_controller.fetch_emails_by_user(username)
            response = json.dumps([email.to_dict() for email in emails], cls=DateTimeEncoder) if emails else "[]"
        elif message.startswith("DELETE_EMAIL"):
            _, email_id, user_id = message.split('|')
            user = user_id
            action = f"DELETE_EMAIL (id={email_id})"
            logger.info(f"[{action}] user={user} ip={ip}")
            try:
                response = handle_delete_email(mail_controller, email_id, user_id)
            except Exception as e:
                logger.error(f"Lỗi khi xử lý DELETE_EMAIL: {e}")
                response = json.dumps({"success": False, "message": "Lỗi không xác định khi xử lý DELETE_EMAIL"})
        elif message.startswith("LOGOUT"):
            _, username = message.split()
            user = username
            action = "LOGOUT"
            logger.info(f"[{action}] user={user} ip={ip}")
            response = "Đăng xuất thành công"
        else:
            action = "UNKNOWN_COMMAND"
            logger.warning(f"[{action}] user={user} ip={ip} message={message}")
            response = "Lệnh không xác định"
        return response
    except Exception as e:
        logger.error(f"[{action}] user={user} ip={ip} Lỗi xử lý message: {e}")
        return "Lỗi xử lý message"

def handle_delete_email(mail_controller, email_id, user_id):
    """
    Xử lý xóa email với timeout và error handling.
    """
    try:
        logger.info(f"Processing DELETE_EMAIL request: id={email_id}, user={user_id}")

        # Kiểm tra và chuyển đổi email_id sang số nguyên
        try:
            email_id = int(email_id)
        except ValueError:
            logger.error(f"Email ID không hợp lệ: {email_id}")
            return json.dumps({"success": False, "message": "Email ID không hợp lệ"})

        # Thêm timeout cho database operation
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(mail_controller.delete_email, email_id, user_id)
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
            "message": f"Lỗi không xác định khi xử lý DELETE_EMAIL: {e}"
        })

def handle_client(client_socket, main_controller, mail_controller):
    try:
        client_socket.settimeout(30)
        addr = client_socket.getpeername()
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
                response = process_message(message, main_controller, mail_controller, addr)
                send_response_with_ack(client_socket, response)

            except socket.timeout:
                logger.warning(f"Client connection timeout ip={addr[0]} port={addr[1]}")
                break
            except ConnectionError as e:
                logger.error(f"Connection error ip={addr[0]} port={addr[1]}: {e}")
                break
            except Exception as e:
                logger.error(f"Error processing message ip={addr[0]} port={addr[1]}: {e}")
                send_error_response(client_socket, "Internal server error")
                continue

    finally:
        client_socket.close()

def start_server(main_controller, mail_controller):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Cho phép reuse address để tránh lỗi WinError 10048 khi restart server nhanh
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind((SERVER_HOST, SERVER_PORT))
    except OSError as e:
        logger.error(f"Lỗi khi bind socket: {e}. Có thể port {SERVER_PORT} đã bị chiếm dụng.")
        print(f"Không thể khởi động server trên port {SERVER_PORT}. Có thể port đã bị chiếm dụng.")
        return
    server.listen(5)
    logger.info(f"Máy chủ đang lắng nghe trên cổng {SERVER_PORT}")

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
