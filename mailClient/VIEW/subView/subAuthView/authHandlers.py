from tkinter import messagebox
from VIEW.mailView import MailView

def handle_login_response(root, username):
    messagebox.showinfo("Đăng nhập", "Đăng nhập thành công")
    MailView(root, username)

def handle_register_response(response):
    if response == "Đăng ký thành công":
        messagebox.showinfo("Đăng ký", "Đăng ký thành công")
    else:
        messagebox.showerror("Đăng ký", response)
