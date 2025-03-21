# Hướng dẫn sử dụng Controller trong thư mục `mailClient`

## Tổng quan
Thư mục `mailClient` chứa các thành phần Controller của ứng dụng Mail Client. Các Controller chịu trách nhiệm xử lý logic nghiệp vụ và tương tác với máy chủ. Dưới đây là mô tả chi tiết về các Controller chính trong thư mục này.

## Các thành phần chính

### 1. `mainController.py`
- **Chức năng**: Xử lý các yêu cầu đăng nhập và đăng ký từ người dùng.
- **Phương thức chính**:
  - `handle_login(username, password)`: Xử lý logic đăng nhập.
  - `handle_register(username, password)`: Xử lý logic đăng ký.

### 2. `authController.py`
- **Chức năng**: Quản lý xác thực người dùng, bao gồm đăng nhập và đăng ký.
- **Phương thức chính**:
  - `login(username, password)`: Kiểm tra thông tin đăng nhập và trả về kết quả.
  - `register(username, password)`: Đăng ký người dùng mới và gửi yêu cầu đến máy chủ.

### 3. `mailController.py`
- **Chức năng**: Quản lý các hoạt động liên quan đến email như gửi email, truy xuất email và người dùng.
- **Phương thức chính**:
  - `send_email(sender, recipients, cc, bcc, subject, body, attachments)`: Gửi email và gửi yêu cầu đến máy chủ.
  - `fetch_emails(username, email_type)`: Truy xuất email dựa trên loại email (inbox, sent).
  - `fetch_all_emails(username)`: Truy xuất tất cả email từ máy chủ.

## Cách sử dụng `mailController`

### 1. Khởi tạo `MailController`
```python
from CONTROLLER.mailController import MailController

mail_controller = MailController(view)
```

### 2. Gửi email
```python
response = mail_controller.send_email(
    sender="sender@example.com",
    recipients="recipient@example.com",
    cc="cc@example.com",
    bcc="bcc@example.com",
    subject="Subject of the email",
    body="Body of the email",
    attachments="path/to/attachment"
)
print(response)
```

### 3. Truy xuất email
```python
# Truy xuất email loại inbox
emails = mail_controller.fetch_emails("username", "inbox")
print(emails)

# Truy xuất email loại sent
emails = mail_controller.fetch_emails("username", "sent")
print(emails)
```

### 4. Truy xuất tất cả email
```python
all_emails = mail_controller.fetch_all_emails("username")
print(all_emails)
```

## Cách hoạt động

1. **Xử lý đăng nhập và đăng ký**:
   - Khi người dùng nhập thông tin đăng nhập hoặc đăng ký, `mainController.py` sẽ gọi các phương thức tương ứng trong `authController.py` để xử lý.
   - `authController.py` sẽ gửi yêu cầu đến máy chủ và trả về kết quả cho `mainController.py`.

2. **Quản lý email**:
   - Khi người dùng gửi email, `mailController.py` sẽ xử lý thông tin và gửi yêu cầu đến máy chủ.
   - Khi người dùng yêu cầu truy xuất email hoặc danh sách người dùng, `mailController.py` sẽ gửi yêu cầu đến máy chủ và trả về kết quả.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của các Controller trong thư mục `mailClient`.
