# Hướng dẫn sử dụng Controller trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần Controller của ứng dụng Mail Server. Các Controller chịu trách nhiệm xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu. Dưới đây là mô tả chi tiết về các Controller chính trong thư mục này.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **Giao thức TCP/IP**: Kết nối client-server.
- **Loguru 0.7.3**: Ghi log.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu.
- **twisted 24.11.0**: Xử lý kết nối mạng không đồng bộ.

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

## Nguyên tắc thiết kế
- **Tách biệt mối quan tâm (Separation of Concerns - SoC)**: Tách biệt rõ ràng giữa lớp trình diễn và lớp logic kinh doanh.
- **Nguyên tắc đơn nhiệm (Single Responsibility Principle - SRP)**: Mỗi lớp chỉ thực hiện một nhiệm vụ duy nhất.
- **Nguyên tắc đảo ngược phụ thuộc (Dependency Inversion Principle - DIP)**: Sử dụng các giao diện và các lớp trừu tượng để giảm thiểu sự phụ thuộc.
- **Mẫu thiết kế MVC (Model-View-Controller)**: Áp dụng mẫu thiết kế MVC để tách biệt rõ ràng giữa các lớp.

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
