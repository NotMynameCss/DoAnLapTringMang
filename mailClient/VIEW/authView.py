import tkinter as tk
from tkinter import messagebox
from CONTROLLER.authController import AuthController
from VIEW.mailView import MailView
from VIEW.subView.subAuthView.entryFrame import EntryFrame
from VIEW.subView.subAuthView.buttonFrame import ButtonFrame

class AuthView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Đăng nhập/Đăng ký")
        self.root.configure(background="gray82")

        # Khung nhập liệu
        self.entry_frame = EntryFrame(self.root)

        # Khung nút
        self.button_frame = ButtonFrame(self.root, self.login, self.register)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_auth(self):
        """Hiển thị giao diện đăng nhập/đăng ký."""
        self.clear_window()
        self.entry_frame = EntryFrame(self.root)
        self.button_frame = ButtonFrame(self.root, self.login, self.register)

    def login(self):
        username = self.entry_frame.username_entry.get().strip()
        password = self.entry_frame.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Lỗi", "Tài khoản và mật khẩu không được để trống.")
            return

        if len(username) < 1 or len(password) < 1:
            messagebox.showerror("Lỗi", "Tài khoản phải có ít nhất 1 ký tự và mật khẩu phải có ít nhất 1 ký tự.")
            return

        auth_controller = AuthController(self)
        response = auth_controller.login(username, password)
        if "thành công" in response.lower():
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công")
            self.clear_window()
            MailView(self.root, username)
        else:
            messagebox.showerror("Đăng nhập", response)

    def register(self):
        username = self.entry_frame.username_entry.get().strip()
        password = self.entry_frame.password_entry.get().strip()
        confirm_password = self.entry_frame.confirm_password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Lỗi", "Tài khoản và mật khẩu không được để trống.")
            return

        if (len(username) < 1 and len(password) < 1):
            messagebox.showerror("Lỗi", "Tài khoản phải có ít nhất 1 ký tự và mật khẩu phải có ít nhất 1 ký tự.")
            return

        if password != confirm_password:
            messagebox.showerror("Đăng ký", "Mật khẩu không khớp.")
            return

        auth_controller = AuthController(self)
        response = auth_controller.register(username, password)
        if "thành công" in response.lower():
            messagebox.showinfo("Đăng ký", "Đăng ký thành công")
        else:
            messagebox.showerror("Đăng ký", response)

    def set_controller(self, controller):
        self.controller = controller
