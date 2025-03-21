# Hướng dẫn sử dụng Controller trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần Controller của ứng dụng Mail Server. Các Controller chịu trách nhiệm xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu. Dưới đây là mô tả chi tiết về các Controller chính trong thư mục này.

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
  - `register(username, password)`: Đăng ký người dùng mới và lưu thông tin vào cơ sở dữ liệu.
- **Chi tiết**:
  - `verify_table_exists()`: Kiểm tra và tạo bảng `users` nếu chưa tồn tại trong cơ sở dữ liệu.

### 3. `mailController.py`
- **Chức năng**: Quản lý các hoạt động liên quan đến email như gửi email, truy xuất email và người dùng.
- **Phương thức chính**:
  - `send_email(sender, recipients, cc, bcc, subject, body, attachments)`: Gửi email và lưu thông tin vào cơ sở dữ liệu.
  - `fetch_emails(email_type)`: Truy xuất email dựa trên loại email (inbox, sent).
  - `fetch_all_emails()`: Truy xuất tất cả email từ cơ sở dữ liệu.
  - `fetch_all_users()`: Truy xuất tất cả người dùng từ cơ sở dữ liệu.
  - `fetch_emails_by_user(username)`: Truy xuất email dựa trên tên người dùng.
  - `refresh_emails()`: Làm mới danh sách email.

## Cách sử dụng `mailController`

### 1. Khởi tạo `MailController`
```python
from CONTROLLER.mailController import MailController

mail_controller = MailController()
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
emails = mail_controller.fetch_emails("inbox")
print(emails)

# Truy xuất email loại sent
emails = mail_controller.fetch_emails("sent")
print(emails)
```

### 4. Truy xuất tất cả email
```python
all_emails = mail_controller.fetch_all_emails()
print(all_emails)
```

### 5. Truy xuất tất cả người dùng
```python
all_users = mail_controller.fetch_all_users()
print(all_users)
```

### 6. Truy xuất email dựa trên tên người dùng
```python
user_emails = mail_controller.fetch_emails_by_user("username")
print(user_emails)
```

### 7. Làm mới danh sách email
```python
refreshed_emails = mail_controller.refresh_emails()
print(refreshed_emails)
```

## Cách hoạt động

1. **Xử lý đăng nhập và đăng ký**:
   - Khi người dùng nhập thông tin đăng nhập hoặc đăng ký, `mainController.py` sẽ gọi các phương thức tương ứng trong `authController.py` để xử lý.
   - `authController.py` sẽ kiểm tra thông tin người dùng trong cơ sở dữ liệu và trả về kết quả cho `mainController.py`.

2. **Quản lý email**:
   - Khi người dùng gửi email, `mailController.py` sẽ xử lý thông tin và lưu vào cơ sở dữ liệu.
   - Khi người dùng yêu cầu truy xuất email hoặc danh sách người dùng, `mailController.py` sẽ truy vấn cơ sở dữ liệu và trả về kết quả.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của các Controller trong thư mục `mailSv`.
