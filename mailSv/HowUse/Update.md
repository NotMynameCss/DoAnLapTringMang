# Hướng dẫn sử dụng Controller trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần Controller của ứng dụng Mail Server. Các Controller chịu trách nhiệm xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **Giao thức TCP/IP**: Kết nối client-server qua cổng `65432`.
- **Loguru 0.7.3**: Ghi log chi tiết.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu trước khi lưu vào cơ sở dữ liệu.

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

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của các Controller trong thư mục `mailSv`.
