# Hướng dẫn sử dụng Database trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần liên quan đến cơ sở dữ liệu của ứng dụng Mail Server. Các thành phần này chịu trách nhiệm kết nối, tạo bảng và thực hiện các thao tác CRUD (Create, Read, Update, Delete) trên cơ sở dữ liệu.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **MySQL**: Hệ quản trị cơ sở dữ liệu.

## Các thành phần chính

### 1. `dbconnector.py`
- **Chức năng**: Kết nối đến cơ sở dữ liệu MySQL và tạo bảng nếu chưa tồn tại.
- **Phương thức chính**:
  - `create_connection()`: Tạo kết nối đến cơ sở dữ liệu MySQL.
  - `create_email_table(connection)`: Tạo bảng `emails` nếu chưa tồn tại trong cơ sở dữ liệu.

### 2. `mailController.py`
- **Chức năng**: Thực hiện các thao tác liên quan đến email trên cơ sở dữ liệu.
- **Phương thức chính**:
  - `send_email(sender, recipients, cc, bcc, subject, body, attachments)`: Gửi email và lưu thông tin vào bảng `emails`.
  - `fetch_emails(email_type)`: Truy xuất email dựa trên loại email (inbox, sent).
  - `fetch_all_emails()`: Truy xuất tất cả email từ bảng `emails`.
  - `fetch_all_users()`: Truy xuất tất cả người dùng từ bảng `users`.
  - `fetch_emails_by_user(username)`: Truy xuất email dựa trên tên người dùng.
  - `search_emails(query)`: Tìm kiếm email dựa trên từ khóa.

### 3. `authController.py`
- **Chức năng**: Thực hiện các thao tác liên quan đến người dùng trên cơ sở dữ liệu.
- **Phương thức chính**:
  - `login(username, password)`: Kiểm tra thông tin đăng nhập của người dùng.
  - `register(username, password)`: Đăng ký người dùng mới và lưu thông tin vào bảng `users`.
  - `verify_table_exists()`: Kiểm tra và tạo bảng `users` nếu chưa tồn tại trong cơ sở dữ liệu.

## Cách hoạt động

1. **Kết nối đến cơ sở dữ liệu**:
   - `dbconnector.py` chứa hàm `create_connection()` để tạo kết nối đến cơ sở dữ liệu MySQL.
   - Khi khởi tạo `MailController` hoặc `AuthController`, hàm `create_connection()` sẽ được gọi để thiết lập kết nối.

2. **Tạo bảng trong cơ sở dữ liệu**:
   - `dbconnector.py` chứa hàm `create_email_table(connection)` để tạo bảng `emails` nếu chưa tồn tại.
   - `AuthController` chứa hàm `verify_table_exists()` để kiểm tra và tạo bảng `users` nếu chưa tồn tại.

3. **Thao tác với bảng `emails`**:
   - `MailController` chứa các phương thức `send_email()`, `fetch_emails()`, `fetch_all_emails()`, `fetch_emails_by_user()`, `search_emails()` để thực hiện các thao tác gửi email và truy xuất email từ bảng `emails`.

4. **Thao tác với bảng `users`**:
   - `AuthController` chứa các phương thức `login()`, `register()` để thực hiện các thao tác đăng nhập và đăng ký người dùng.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của cơ sở dữ liệu trong thư mục `mailSv`.
