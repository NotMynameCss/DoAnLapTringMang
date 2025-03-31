# Hướng dẫn sử dụng View trong thư mục `mailSv`

## Tổng quan
Hệ thống view trong `mailSv` được xây dựng theo mô hình MVC, sử dụng Tkinter cho GUI. Giao diện được tách thành các module nhỏ để dễ bảo trì và mở rộng.

## Công nghệ
- Python 3.13.2
- Tkinter: GUI Framework
- Loguru 0.7.3: Logging
- Threading: Xử lý đa luồng

## Cấu trúc View

### 1. Giao diện chính 
- **mailView.py**: Giao diện chính sau đăng nhập
  ```python
  # Khởi tạo giao diện
  root = tk.Tk()
  mail_view = MailView(root, username)
  ```

### 2. Phân cấp View
```
mailSv/
└── VIEW/
    ├── mailView.py           # Giao diện chính
    ├── authView.py           # Giao diện đăng nhập
    ├── mailSendView.py       # Giao diện gửi mail
    └── subView/
        ├── subMailView/
        │   ├── topFrame.py   # Thanh công cụ
        │   ├── leftFrame.py  # Menu trái
        │   └── rightFrame.py # Nội dung chính
        └── subAuthView/
            ├── entryFrame.py # Form nhập liệu
            └── buttonFrame.py # Nút bấm
```

### 3. Các thành phần giao diện

#### TopFrame
- Thanh công cụ chính
- Chức năng:
  - Soạn thư mới
  - Tìm kiếm 
  - Làm mới
  - Xem tất cả email

#### LeftFrame 
- Menu điều hướng
- Các mục:
  - Hộp thư đến
  - Đã gửi
  - Thư nháp 
  - Thùng rác
  - Nhãn
  - Cài đặt
  - Chat/Meet
  - Xóa mail

#### RightFrame
- Hiển thị danh sách và chi tiết email
- Tính năng:
  - Xem danh sách email
  - Xem chi tiết email
  - Xóa email
  - Làm mới danh sách

## Cách sử dụng

### 1. Khởi tạo View
```python
# Khởi tạo giao diện chính
root = tk.Tk()
mail_view = MailView(root, username)

# Khởi tạo giao diện gửi mail
send_window = tk.Toplevel()
mail_send_view = MailSendView(send_window, username)
```

### 2. Xử lý sự kiện
```python
# Gửi email
def send_email(self):
    email_data = {
        "sender": self.username,
        "recipients": self.to_entry.get(),
        "subject": self.subject_entry.get(),
        "body": self.body_text.get("1.0", tk.END)
    }
    response = self.mail_controller.send_email(email_data)
```

### 3. Cập nhật giao diện
```python 
def refresh_emails(self):
    """Làm mới danh sách email"""
    emails = self.mail_controller.fetch_emails("inbox")
    self.right_frame.update_email_list(emails)
```

## Xử lý lỗi

### 1. Validate dữ liệu
```python
def validate_input(self):
    if not self.to_entry.get():
        messagebox.showerror("Lỗi", "Vui lòng nhập người nhận")
        return False
    return True
```

### 2. Try-except
```python
try:
    response = self.mail_controller.send_email(data)
except Exception as e:
    logger.error(f"Lỗi gửi email: {e}")
    messagebox.showerror("Lỗi", str(e))
```

## Best Practices

1. **Tách biệt View**:
- Mỗi view trong file riêng
- Chia nhỏ thành subview
- Tái sử dụng components

2. **Xử lý lỗi**: 
- Validate input
- Try-except blocks
- Thông báo lỗi rõ ràng

3. **Threading**:
- Tải dữ liệu không đồng bộ
- Không block UI
- Cập nhật UI an toàn

4. **Logging**:
- Log mọi lỗi
- Debug thông tin
- Rotation logs

## Kế hoạch phát triển

1. **UI/UX**:
- Thêm themes
- Responsive design
- Animations

2. **Tính năng**:
- Rich text editor
- Drag & drop files
- Tìm kiếm nâng cao

3. **Hiệu suất**:
- Lazy loading
- Caching
- Virtual scrolling
