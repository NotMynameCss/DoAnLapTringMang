import tkinter as tk

class EntryFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="gray82")
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Nhập tài khoản
        self.username_label = tk.Label(self, text="Tài khoản:", bg="gray82", anchor="w")
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = tk.Entry(self, bg="white")
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Nhập mật khẩu
        self.password_label = tk.Label(self, text="Mật khẩu:", bg="gray82", anchor="w")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = tk.Entry(self, bg="white", show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Nhập lại mật khẩu
        self.confirm_password_label = tk.Label(self, text="Nhập lại mật khẩu:", bg="gray82", anchor="w")
        self.confirm_password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.confirm_password_entry = tk.Entry(self, bg="white", show="*")
        self.confirm_password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Cấu hình lưới
        self.columnconfigure(1, weight=1)
