import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from CONTROLLER.mailController import MailController

class MailSendView:
    def __init__(self, root):
        self.root = root
        self.root.title("Soạn Email")
        self.root.geometry("800x600")
        self.root.configure(background="white")

        self.mail_controller = MailController(self)

        # Tạo khung chính
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo khung trên cùng cho địa chỉ email
        self.top_frame = tk.Frame(self.main_frame, bg="white")
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tk.Label(self.top_frame, text="To:", bg="white").grid(row=0, column=0, sticky=tk.W)
        self.to_entry = tk.Entry(self.top_frame, width=80)
        self.to_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.top_frame, text="Cc:", bg="white").grid(row=1, column=0, sticky=tk.W)
        self.cc_entry = tk.Entry(self.top_frame, width=80)
        self.cc_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.top_frame, text="Bcc:", bg="white").grid(row=2, column=0, sticky=tk.W)
        self.bcc_entry = tk.Entry(self.top_frame, width=80)
        self.bcc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Tạo khung cho tiêu đề
        self.subject_frame = tk.Frame(self.main_frame, bg="white")
        self.subject_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tk.Label(self.subject_frame, text="Subject:", bg="white").pack(side=tk.LEFT)
        self.subject_entry = tk.Entry(self.subject_frame, width=80)
        self.subject_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Tạo khung cho nội dung email
        self.body_frame = tk.Frame(self.main_frame, bg="white")
        self.body_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.body_text = tk.Text(self.body_frame, wrap=tk.WORD)
        self.body_text.pack(fill=tk.BOTH, expand=True)

        # Tạo khung dưới cùng cho các nút và tệp đính kèm
        self.bottom_frame = tk.Frame(self.main_frame, bg="white")
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.attach_button = tk.Button(self.bottom_frame, text="Đính kèm tệp", command=self.attach_file)
        self.attach_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.send_button = tk.Button(self.bottom_frame, text="Gửi", command=self.send_email)
        self.send_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.save_draft_button = tk.Button(self.bottom_frame, text="Lưu nháp", command=self.save_draft)
        self.save_draft_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def attach_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Tệp đính kèm", f"Tệp đã được đính kèm: {file_path}")

    def send_email(self):
        sender = "client@example.com"  # Thay thế bằng email người gửi thực tế
        recipients = self.to_entry.get()
        cc = self.cc_entry.get()
        bcc = self.bcc_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END)
        attachments = ""  # Thực hiện xử lý tệp đính kèm
        response = self.mail_controller.send_email(sender, recipients, cc, bcc, subject, body, attachments)
        if response == "Email đã được gửi thành công":
            messagebox.showinfo("Gửi Email", response)
        else:
            messagebox.showerror("Gửi Email", response)

    def save_draft(self):
        # Thực hiện logic lưu nháp tại đây
        messagebox.showinfo("Lưu nháp", "Bản nháp đã được lưu thành công")

if __name__ == "__main__":
    root = tk.Tk()
    app = MailSendView(root)
    root.mainloop()
