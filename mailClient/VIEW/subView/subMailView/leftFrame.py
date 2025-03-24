import tkinter as tk

class LeftFrame(tk.Frame):
    def __init__(self, parent, mail_view):
        super().__init__(parent, bg="white")
        self.mail_view = mail_view

        self.nav_frame = tk.Frame(self, bg="white")
        self.nav_frame.grid(row=0, column=0, sticky="nsew")

        self.inbox_button = tk.Button(self.nav_frame, text="Hộp thư đến", command=self.mail_view.show_inbox)
        self.inbox_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.sent_button = tk.Button(self.nav_frame, text="Đã gửi", command=self.mail_view.show_sent)
        self.sent_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.drafts_button = tk.Button(self.nav_frame, text="Thư nháp", command=self.mail_view.show_drafts)
        self.drafts_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.trash_button = tk.Button(self.nav_frame, text="Thùng rác", command=self.mail_view.show_trash)
        self.trash_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.labels_button = tk.Button(self.nav_frame, text="Nhãn", command=self.mail_view.show_labels)
        self.labels_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.settings_button = tk.Button(self.nav_frame, text="Cài đặt", command=self.mail_view.show_settings)
        self.settings_button.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        self.chat_button = tk.Button(self.nav_frame, text="Chat/Meet", command=self.mail_view.show_chat)
        self.chat_button.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
