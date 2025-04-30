import tkinter as tk

class TopFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.compose_button = tk.Button(self, text="Soạn thư", command=self.mail_view.compose_email)
        self.compose_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.search_entry = tk.Entry(self, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.search_button = tk.Button(self, text="Tìm Kiếm", command=self.mail_view.search_email)
        self.search_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.refresh_button = tk.Button(self, text="Làm mới", command=self.mail_view.refresh_emails)
        self.refresh_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Thêm nút Đăng xuất
        self.logout_button = tk.Button(self, text="Đăng xuất", command=self.mail_view.logout)
        self.logout_button.pack(side=tk.RIGHT, padx=5, pady=5)
