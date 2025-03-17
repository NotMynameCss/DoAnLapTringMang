
import tkinter as tk
from tkinter import messagebox
from CONTROLLER.authController import AuthController

class AuthView:
    def __init__(self, root):
        self.root = root

    def show_auth(self):
        self.clear_window()
        self.root.title("Đăng nhập/Đăng ký")

        tk.Label(self.root, text="Tên người dùng").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Mật khẩu").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Đăng nhập", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Đăng ký", command=self.register).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Call the login controller function
        auth_controller = AuthController(self)
        response = auth_controller.login(username, password)
        if response == "Đăng nhập thành công":
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công")
        else:
            messagebox.showerror("Đăng nhập", response)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Call the register controller function
        auth_controller = AuthController(self)
        response = auth_controller.register(username, password)
        if response == "Đăng ký thành công":
            messagebox.showinfo("Đăng ký", "Đăng ký thành công")
        else:
            messagebox.showerror("Đăng ký", response)

    def set_controller(self, controller):
        self.controller = controller
