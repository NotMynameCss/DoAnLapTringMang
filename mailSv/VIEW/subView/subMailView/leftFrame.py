import tkinter as tk

class LeftFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.inbox_button = tk.Button(self, text="Hộp thư đến", command=self.mail_view.show_inbox)
        self.inbox_button.pack(fill=tk.X, padx=10, pady=5)

        self.sent_button = tk.Button(self, text="Đã gửi", command=self.mail_view.show_sent)
        self.sent_button.pack(fill=tk.X, padx=10, pady=5)

        self.drafts_button = tk.Button(self, text="Thư nháp", command=self.mail_view.show_drafts)
        self.drafts_button.pack(fill=tk.X, padx=10, pady=5)

        self.trash_button = tk.Button(self, text="Thùng rác", command=self.mail_view.show_trash)
        self.trash_button.pack(fill=tk.X, padx=10, pady=5)

        self.labels_button = tk.Button(self, text="Nhãn", command=self.mail_view.show_labels)
        self.labels_button.pack(fill=tk.X, padx=10, pady=5)

        self.settings_button = tk.Button(self, text="Cài đặt", command=self.mail_view.show_settings)
        self.settings_button.pack(fill=tk.X, padx=10, pady=5)

        self.chat_button = tk.Button(self, text="Chat/Meet", command=self.mail_view.show_chat)
        self.chat_button.pack(fill=tk.X, padx=10, pady=5)

        # Thêm nút Xóa Mail
        self.delete_mail_button = tk.Button(self, text="Xóa Mail", command=self.mail_view.delete_email)
        self.delete_mail_button.pack(fill=tk.X, padx=10, pady=5)

