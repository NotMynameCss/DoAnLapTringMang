# khắc lỗi đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# giao diện
import tkinter as tk
from VIEW.authView import AuthView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Client")
        self.root.geometry("400x400")

        self.auth_view = AuthView(self.root)
        self.auth_view.show_auth()  # Gọi phương thức show_auth() để hiển thị giao diện đăng nhập/đăng ký

    def set_controller(self, controller):
        self.auth_view.set_controller(controller)
