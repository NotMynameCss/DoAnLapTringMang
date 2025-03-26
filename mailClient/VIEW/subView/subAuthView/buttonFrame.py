import tkinter as tk

class ButtonFrame(tk.Frame):
    def __init__(self, parent, login_callback, register_callback):
        super().__init__(parent, bg="gray82")
        self.pack(fill=tk.X, padx=10, pady=10)

        # Nút Đăng nhập
        self.login_button = tk.Button(self, text="Đăng nhập", command=login_callback, bg="white")
        self.login_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Nút Đăng ký
        self.register_button = tk.Button(self, text="Đăng ký", command=register_callback, bg="white")
        self.register_button.pack(side=tk.RIGHT, padx=5, pady=5)
