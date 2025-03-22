import tkinter as tk

class TopFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.compose_button = tk.Button(self, text="Soạn Thư", command=self.mail_view.compose_email)
        self.compose_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.search_entry = tk.Entry(self, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.search_button = tk.Button(self, text="Tìm Kiếm", command=self.mail_view.search_email)
        self.search_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Add refresh button
        self.refresh_button = tk.Button(self, text="Làm mới", command=self.mail_view.refresh_emails)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)
