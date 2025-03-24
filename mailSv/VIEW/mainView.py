# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# giao diện
import tkinter as tk
from VIEW.authView import AuthView
from VIEW.mailView import MailView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Server")
        self.root.geometry("400x400")

        self.auth_view = AuthView(self.root, self)
        self.auth_view.show_auth()

    def set_controller(self, controller):
        self.auth_view.set_controller(controller)

    def show_mail_view(self, username):
        self.auth_view.clear_window()
        MailView(self.root, username)
