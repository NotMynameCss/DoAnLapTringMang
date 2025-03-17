# khắc lỗi đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# giao diện
import tkinter as tk
from .authView import AuthView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Client")
        self.root.geometry("400x400")

        self.auth_view = AuthView(self.root)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Giao diện mail client", font=("Arial", 16))
        self.label.pack(pady=20)

        self.auth_view.show_auth()

    def set_controller(self, controller):
        self.auth_view.set_controller(controller)
