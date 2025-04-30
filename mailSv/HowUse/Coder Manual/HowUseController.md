# Hướng dẫn sử dụng Controller trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần Controller của ứng dụng Mail Server. Các Controller chịu trách nhiệm xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu.

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

### 3. `mailController.py`
- **Chức năng**: Quản lý các hoạt động liên quan đến email như gửi email, truy xuất email, và xóa email.
- **Phương thức chính**:
  - `send_email(sender, recipients, cc, bcc, subject, body, attachments)`: Gửi email và lưu thông tin vào cơ sở dữ liệu.
  - `fetch_emails(email_type)`: Truy xuất email dựa trên loại email (inbox, sent).
  - `fetch_all_emails()`: Truy xuất tất cả email từ cơ sở dữ liệu.
  - `fetch_all_users()`: Truy xuất tất cả người dùng từ cơ sở dữ liệu.
  - `fetch_emails_by_user(username, email_type)`: Truy xuất email dựa trên tên người dùng.
  - `delete_email(email_id, user_id)`: Xóa email của người dùng.
  - `refresh_emails()`: Làm mới danh sách email.

## Cải tiến mới
- **Decorator `retry_with_limit`**: Giới hạn số lần thử lại khi xảy ra lỗi.
- **Connection Pooling**: Kích hoạt Connection Pooling trong SQLAlchemy để cải thiện hiệu suất.
- **Xử lý lỗi TCP**: Thêm cơ chế timeout và acknowledgment (ACK) để đảm bảo tính ổn định.



