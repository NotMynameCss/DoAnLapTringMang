# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# giao diện
import tkinter as tk
from tkinter import messagebox
from CONTROLLER.authController import AuthController
from twisted.internet import reactor
from VIEW.subView.subAuthView.entryFrame import EntryFrame
from VIEW.subView.subAuthView.buttonFrame import ButtonFrame
from VIEW.subView.subAuthView.authHandlers import handle_login_response, handle_register_response

class AuthView:
    def __init__(self, root, main_view):
        self.root = root
        self.main_view = main_view
        self.root.geometry("300x200+523+226")
        self.root.minsize(120, 1)
        self.root.maxsize(1924, 1061)
        self.root.resizable(1, 1)
        self.root.title("Đăng nhập/Đăng ký")
        self.root.configure(background="gray82")
        self.root.configure(highlightbackground="gray82")
        self.root.configure(highlightcolor="black")

        self.entry_frame = EntryFrame(self.root, self)
        self.entry_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        self.button_frame = ButtonFrame(self.root, self)
        self.button_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.entry_frame.username_entry.get()
        password = self.entry_frame.password_entry.get()
        auth_controller = AuthController(self)
        response = auth_controller.login(username, password)
        if response == "Đăng nhập thành công":
            handle_login_response(self.main_view, username)
        else:
            messagebox.showerror("Đăng nhập", response)

    def register(self):
        username = self.entry_frame.username_entry.get()
        password = self.entry_frame.password_entry.get()
        auth_controller = AuthController(self)
        response = auth_controller.register(username, password)
        reactor.callFromThread(handle_register_response, response)

    def set_controller(self, controller):
        self.controller = controller

    def show_auth(self):
        self.clear_window()
        self.root.title("Đăng nhập/Đăng ký")
        self.entry_frame = EntryFrame(self.root, self)
        self.entry_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.button_frame = ButtonFrame(self.root, self)
        self.button_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
