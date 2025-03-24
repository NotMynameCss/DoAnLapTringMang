import tkinter as tk

class ButtonFrame(tk.Frame):
    def __init__(self, parent, auth_view):
        super().__init__(parent, bg="gray82")
        self.auth_view = auth_view

        self.login_button = tk.Button(self, text="Đăng nhập", command=self.auth_view.login)
        self.login_button.place(relx=0.367, rely=0.1, height=26, width=67)
        self.login_button.configure(activebackground="#d9d9d9")
        self.login_button.configure(activeforeground="black")
        self.login_button.configure(background="gray82")
        self.login_button.configure(disabledforeground="#9d9d9d")
        self.login_button.configure(foreground="black")
        self.login_button.configure(highlightbackground="gray82")
        self.login_button.configure(highlightcolor="black")

        self.register_button = tk.Button(self, text="Đăng ký", command=self.auth_view.register)
        self.register_button.place(relx=0.7, rely=0.1, height=26, width=67)
        self.register_button.configure(activebackground="#d9d9d9")
        self.register_button.configure(activeforeground="black")
        self.register_button.configure(background="gray82")
        self.register_button.configure(disabledforeground="#9d9d9d")
        self.register_button.configure(foreground="black")
        self.register_button.configure(highlightbackground="gray82")
        self.register_button.configure(highlightcolor="black")
