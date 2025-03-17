import socket
from tkinter import messagebox

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
            return response
        except Exception as e:
            return f"Lỗi kết nối đến server: {e}"

    def login(self, username, password):
        message = f"LOGIN {username} {password}"
        response = self.send_request(message)
        return response

    def register(self, username, password):
        message = f"REGISTER {username} {password}"
        response = self.send_request(message)
        return response
