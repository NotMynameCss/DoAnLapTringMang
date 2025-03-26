import tkinter as tk

class ToolbarFrame(tk.Frame):
    def __init__(self, parent, compose_callback, search_callback, refresh_callback, show_all_callback):
        super().__init__(parent, bg="white")
        self.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Nút Soạn Thư
        self.compose_button = tk.Button(self, text="Soạn Thư", command=compose_callback)
        self.compose_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Ô tìm kiếm
        self.search_entry = tk.Entry(self, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Nút Tìm Kiếm
        self.search_button = tk.Button(self, text="Tìm Kiếm", command=search_callback)
        self.search_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Nút Làm mới
        self.refresh_button = tk.Button(self, text="Làm mới", command=refresh_callback)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Nút Tất cả Email
        self.all_emails_button = tk.Button(self, text="Tất cả Email", command=show_all_callback)
        self.all_emails_button.pack(side=tk.LEFT, padx=10, pady=10)
