import socket
import json

class MailController:
    def __init__(self, view):
        self.view = view

    def send_request(self, message):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 65432))
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            client_socket.close()
            return response
        except Exception as e:
            return f"Lỗi kết nối đến server: {e}"

    def send_email(self, sender, recipients, cc, bcc, subject, body, attachments):
        message = f"SEND_EMAIL|{sender}|{recipients}|{cc}|{bcc}|{subject}|{body}|{attachments}"
        response = self.send_request(message)
        return response

    def fetch_emails(self, username, email_type):
        message = f"FETCH_EMAILS|{username}|{email_type}"
        response = self.send_request(message)
        try:
            emails = json.loads(response) if response else []
        except json.JSONDecodeError as e:
            print(f"Lỗi khi phân tích cú pháp email: {e}")
            emails = []
        return emails

    def fetch_all_emails(self, username):
        message = f"FETCH_ALL_EMAILS|{username}"
        response = self.send_request(message)
        try:
            emails = json.loads(response) if response else []
        except json.JSONDecodeError as e:
            print(f"Lỗi khi phân tích cú pháp email: {e}")
            emails = []
        return emails
