import tkinter as tk

class LeftFrame(tk.Frame):
    def __init__(self, parent, inbox_callback, sent_callback, drafts_callback, trash_callback, labels_callback, settings_callback, chat_callback):
        super().__init__(parent, bg="white")
        self.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Nút Hộp thư đến
        self.inbox_button = tk.Button(self, text="Hộp thư đến", command=inbox_callback)
        self.inbox_button.pack(fill=tk.X, padx=10, pady=5)

        # Nút Đã gửi
        self.sent_button = tk.Button(self, text="Đã gửi", command=sent_callback)
        self.sent_button.pack(fill=tk.X, padx=10, pady=5)

        # Nút Thư nháp
        self.drafts_button = tk.Button(self, text="Thư nháp", command=drafts_callback)
        self.drafts_button.pack(fill=tk.X, padx=10, pady=5)

        # Nút Thùng rác
        self.trash_button = tk.Button(self, text="Thùng rác", command=trash_callback)
        self.trash_button.pack(fill=tk.X, padx=10, pady=5)

        # Nút Nhãn
        self.labels_button = tk.Button(self, text="Nhãn", command=labels_callback)
        self.labels_button.pack(fill=tk.X, padx=10, pady=5)

        # Nút Cài đặt
        self.settings_button = tk.Button(self, text="Cài đặt", command=settings_callback)
        self.settings_button.pack(fill=tk.X, padx=10, pady=5)

        # Nút Chat/Meet
        self.chat_button = tk.Button(self, text="Chat/Meet", command=chat_callback)
        self.chat_button.pack(fill=tk.X, padx=10, pady=5)
