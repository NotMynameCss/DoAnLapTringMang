import tkinter as tk
from tkinter import messagebox
from CONTROLLER.authController import AuthController
from VIEW.mailView import MailView

class AuthView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200+523+226")
        self.root.minsize(120, 1)
        self.root.maxsize(1924, 1061)
        self.root.resizable(1, 1)
        self.root.title("Đăng nhập/Đăng ký")
        self.root.configure(background="gray82")
        self.root.configure(highlightbackground="gray82")
        self.root.configure(highlightcolor="black")

        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(relx=0.367, rely=0.1, height=17, relwidth=0.613)
        self.username_entry.configure(background="gray82")
        self.username_entry.configure(disabledforeground="#9d9d9d")
        self.username_entry.configure(font="TkFixedFont")
        self.username_entry.configure(foreground="black")
        self.username_entry.configure(highlightbackground="gray82")
        self.username_entry.configure(highlightcolor="black")
        self.username_entry.configure(insertbackground="black")
        self.username_entry.configure(selectbackground="#d9d9d9")
        self.username_entry.configure(selectforeground="black")

        self.password_entry = tk.Entry(self.root)
        self.password_entry.place(relx=0.367, rely=0.25, height=17, relwidth=0.613)
        self.password_entry.configure(background="gray82")
        self.password_entry.configure(disabledforeground="#9d9d9d")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="black")
        self.password_entry.configure(highlightbackground="gray82")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="#d9d9d9")
        self.password_entry.configure(selectforeground="black")

        self.confirm_password_entry = tk.Entry(self.root)
        self.confirm_password_entry.place(relx=0.367, rely=0.4, height=17, relwidth=0.613)
        self.confirm_password_entry.configure(background="gray82")
        self.confirm_password_entry.configure(disabledforeground="#9d9d9d")
        self.confirm_password_entry.configure(font="TkFixedFont")
        self.confirm_password_entry.configure(foreground="black")
        self.confirm_password_entry.configure(highlightbackground="gray82")
        self.confirm_password_entry.configure(highlightcolor="black")
        self.confirm_password_entry.configure(insertbackground="black")
        self.confirm_password_entry.configure(selectbackground="#d9d9d9")
        self.confirm_password_entry.configure(selectforeground="black")

        self.username_label = tk.Label(self.root)
        self.username_label.place(relx=0.017, rely=0.11, height=20, width=57)
        self.username_label.configure(activebackground="#d9d9d9")
        self.username_label.configure(activeforeground="black")
        self.username_label.configure(anchor='w')
        self.username_label.configure(background="gray82")
        self.username_label.configure(compound='left')
        self.username_label.configure(disabledforeground="#9d9d9d")
        self.username_label.configure(foreground="black")
        self.username_label.configure(highlightbackground="gray82")
        self.username_label.configure(highlightcolor="black")
        self.username_label.configure(text='''tài khoản''')

        self.password_label = tk.Label(self.root)
        self.password_label.place(relx=0.0, rely=0.25, height=19, width=62)
        self.password_label.configure(activebackground="#d9d9d9")
        self.password_label.configure(activeforeground="black")
        self.password_label.configure(anchor='w')
        self.password_label.configure(background="gray82")
        self.password_label.configure(compound='left')
        self.password_label.configure(disabledforeground="#9d9d9d")
        self.password_label.configure(foreground="black")
        self.password_label.configure(highlightbackground="gray82")
        self.password_label.configure(highlightcolor="black")
        self.password_label.configure(text='''Mật khẩu''')

        self.confirm_password_label = tk.Label(self.root)
        self.confirm_password_label.place(relx=0.0, rely=0.35, height=34, width=107)
        self.confirm_password_label.configure(activebackground="#d9d9d9")
        self.confirm_password_label.configure(activeforeground="black")
        self.confirm_password_label.configure(anchor='w')
        self.confirm_password_label.configure(background="gray82")
        self.confirm_password_label.configure(compound='left')
        self.confirm_password_label.configure(disabledforeground="#9d9d9d")
        self.confirm_password_label.configure(foreground="black")
        self.confirm_password_label.configure(highlightbackground="gray82")
        self.confirm_password_label.configure(highlightcolor="black")
        self.confirm_password_label.configure(text='''Nhập lại mật khẩu\n(Nếu đăng ký)''')

        self.login_button = tk.Button(self.root)
        self.login_button.place(relx=0.367, rely=0.6, height=26, width=67)
        self.login_button.configure(activebackground="#d9d9d9")
        self.login_button.configure(activeforeground="black")
        self.login_button.configure(background="gray82")
        self.login_button.configure(disabledforeground="#9d9d9d")
        self.login_button.configure(foreground="black")
        self.login_button.configure(highlightbackground="gray82")
        self.login_button.configure(highlightcolor="black")
        self.login_button.configure(text='''Đăng nhập''')
        self.login_button.configure(command=self.login)

        self.register_button = tk.Button(self.root)
        self.register_button.place(relx=0.7, rely=0.6, height=26, width=67)
        self.register_button.configure(activebackground="#d9d9d9")
        self.register_button.configure(activeforeground="black")
        self.register_button.configure(background="gray82")
        self.register_button.configure(disabledforeground="#9d9d9d")
        self.register_button.configure(foreground="black")
        self.register_button.configure(highlightbackground="gray82")
        self.register_button.configure(highlightcolor="black")
        self.register_button.configure(text='''Đăng ký''')
        self.register_button.configure(command=self.register)

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
            self.clear_window()
            MailView(self.root, username)  # Switch to MailView with username
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

    def show_auth(self):
        self.clear_window()
        self.root.title("Đăng nhập/Đăng ký")

        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(relx=0.367, rely=0.1, height=17, relwidth=0.613)
        self.username_entry.configure(background="gray82")
        self.username_entry.configure(disabledforeground="#9d9d9d")
        self.username_entry.configure(font="TkFixedFont")
        self.username_entry.configure(foreground="black")
        self.username_entry.configure(highlightbackground="gray82")
        self.username_entry.configure(highlightcolor="black")
        self.username_entry.configure(insertbackground="black")
        self.username_entry.configure(selectbackground="#d9d9d9")
        self.username_entry.configure(selectforeground="black")

        self.password_entry = tk.Entry(self.root)
        self.password_entry.place(relx=0.367, rely=0.25, height=17, relwidth=0.613)
        self.password_entry.configure(background="gray82")
        self.password_entry.configure(disabledforeground="#9d9d9d")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="black")
        self.password_entry.configure(highlightbackground="gray82")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="#d9d9d9")
        self.password_entry.configure(selectforeground="black")

        self.confirm_password_entry = tk.Entry(self.root)
        self.confirm_password_entry.place(relx=0.367, rely=0.4, height=17, relwidth=0.613)
        self.confirm_password_entry.configure(background="gray82")
        self.confirm_password_entry.configure(disabledforeground="#9d9d9d")
        self.confirm_password_entry.configure(font="TkFixedFont")
        self.confirm_password_entry.configure(foreground="black")
        self.confirm_password_entry.configure(highlightbackground="gray82")
        self.confirm_password_entry.configure(highlightcolor="black")
        self.confirm_password_entry.configure(insertbackground="black")
        self.confirm_password_entry.configure(selectbackground="#d9d9d9")
        self.confirm_password_entry.configure(selectforeground="black")

        self.username_label = tk.Label(self.root)
        self.username_label.place(relx=0.017, rely=0.11, height=20, width=57)
        self.username_label.configure(activebackground="#d9d9d9")
        self.username_label.configure(activeforeground="black")
        self.username_label.configure(anchor='w')
        self.username_label.configure(background="gray82")
        self.username_label.configure(compound='left')
        self.username_label.configure(disabledforeground="#9d9d9d")
        self.username_label.configure(foreground="black")
        self.username_label.configure(highlightbackground="gray82")
        self.username_label.configure(highlightcolor="black")
        self.username_label.configure(text='''tài khoản''')

        self.password_label = tk.Label(self.root)
        self.password_label.place(relx=0.0, rely=0.25, height=19, width=62)
        self.password_label.configure(activebackground="#d9d9d9")
        self.password_label.configure(activeforeground="black")
        self.password_label.configure(anchor='w')
        self.password_label.configure(background="gray82")
        self.password_label.configure(compound='left')
        self.password_label.configure(disabledforeground="#9d9d9d")
        self.password_label.configure(foreground="black")
        self.password_label.configure(highlightbackground="gray82")
        self.password_label.configure(highlightcolor="black")
        self.password_label.configure(text='''Mật khẩu''')

        self.confirm_password_label = tk.Label(self.root)
        self.confirm_password_label.place(relx=0.0, rely=0.35, height=34, width=107)
        self.confirm_password_label.configure(activebackground="#d9d9d9")
        self.confirm_password_label.configure(activeforeground="black")
        self.confirm_password_label.configure(anchor='w')
        self.confirm_password_label.configure(background="gray82")
        self.confirm_password_label.configure(compound='left')
        self.confirm_password_label.configure(disabledforeground="#9d9d9d")
        self.confirm_password_label.configure(foreground="black")
        self.confirm_password_label.configure(highlightbackground="gray82")
        self.confirm_password_label.configure(highlightcolor="black")
        self.confirm_password_label.configure(text='''Nhập lại mật khẩu\n(Nếu đăng ký)''')

        self.login_button = tk.Button(self.root)
        self.login_button.place(relx=0.367, rely=0.6, height=26, width=67)
        self.login_button.configure(activebackground="#d9d9d9")
        self.login_button.configure(activeforeground="black")
        self.login_button.configure(background="gray82")
        self.login_button.configure(disabledforeground="#9d9d9d")
        self.login_button.configure(foreground="black")
        self.login_button.configure(highlightbackground="gray82")
        self.login_button.configure(highlightcolor="black")
        self.login_button.configure(text='''Đăng nhập''')
        self.login_button.configure(command=self.login)

        self.register_button = tk.Button(self.root)
        self.register_button.place(relx=0.7, rely=0.6, height=26, width=67)
        self.register_button.configure(activebackground="#d9d9d9")
        self.register_button.configure(activeforeground="black")
        self.register_button.configure(background="gray82")
        self.register_button.configure(disabledforeground="#9d9d9d")
        self.register_button.configure(foreground="black")
        self.register_button.configure(highlightbackground="gray82")
        self.register_button.configure(highlightcolor="black")
        self.register_button.configure(text='''Đăng ký''')
        self.register_button.configure(command=self.register)
