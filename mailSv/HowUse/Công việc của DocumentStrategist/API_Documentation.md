# API Documentation

## Tổng quan
API Documentation cung cấp thông tin chi tiết về các API được sử dụng trong hệ thống mailServer. Các API này chịu trách nhiệm xử lý các yêu cầu từ client và tương tác với cơ sở dữ liệu.

## Công nghệ sử dụng
- **Python 3.11.9**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **Giao thức TCP/IP**: Kết nối client-server.
- **Loguru 0.7.3**: Ghi log.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu.
- **twisted 24.11.0**: Xử lý kết nối mạng không đồng bộ.

## API Endpoints

### 1. Đăng nhập (Login)
- **Endpoint**: `/login`
- **Phương thức**: POST
- **Mô tả**: Kiểm tra thông tin đăng nhập của người dùng.
- **Yêu cầu**:
  - `username` (str): Tên đăng nhập của người dùng.
  - `password` (str): Mật khẩu của người dùng.
- **Phản hồi**:
  - `success` (bool): Trạng thái đăng nhập.
  - `message` (str): Thông báo kết quả đăng nhập.

```json
{
  "username": "example_user",
  "password": "example_password"
}
```

### 2. Đăng ký (Register)
- **Endpoint**: `/register`
- **Phương thức**: POST
- **Mô tả**: Đăng ký người dùng mới.
- **Yêu cầu**:
  - `username` (str): Tên đăng nhập của người dùng.
  - `password` (str): Mật khẩu của người dùng.
- **Phản hồi**:
  - `success` (bool): Trạng thái đăng ký.
  - `message` (str): Thông báo kết quả đăng ký.

```json
{
  "username": "new_user",
  "password": "new_password"
}
```

### 3. Gửi email (Send Email)
- **Endpoint**: `/send_email`
- **Phương thức**: POST
- **Mô tả**: Gửi email và lưu thông tin vào cơ sở dữ liệu.
- **Yêu cầu**:
  - `sender` (str): Địa chỉ email của người gửi.
  - `recipients` (str): Danh sách địa chỉ email của người nhận.
  - `cc` (str): Danh sách địa chỉ email của người nhận CC.
  - `bcc` (str): Danh sách địa chỉ email của người nhận BCC.
  - `subject` (str): Chủ đề của email.
  - `body` (str): Nội dung của email.
  - `attachments` (str): Danh sách tệp đính kèm.
- **Phản hồi**:
  - `success` (bool): Trạng thái gửi email.
  - `message` (str): Thông báo kết quả gửi email.

```json
{
  "sender": "sender@example.com",
  "recipients": "recipient@example.com",
  "cc": "cc@example.com",
  "bcc": "bcc@example.com",
  "subject": "Subject of the email",
  "body": "Body of the email",
  "attachments": "path/to/attachment"
}
```

### 4. Truy xuất email (Fetch Emails)
- **Endpoint**: `/fetch_emails`
- **Phương thức**: GET
- **Mô tả**: Truy xuất email dựa trên loại email (inbox, sent).
- **Yêu cầu**:
  - `email_type` (str): Loại email cần truy xuất (inbox, sent).
- **Phản hồi**:
  - `emails` (list): Danh sách email.

```json
{
  "email_type": "inbox"
}
```

### 5. Truy xuất tất cả email (Fetch All Emails)
- **Endpoint**: `/fetch_all_emails`
- **Phương thức**: GET
- **Mô tả**: Truy xuất tất cả email từ cơ sở dữ liệu.
- **Phản hồi**:
  - `emails` (list): Danh sách tất cả email.

### 6. Truy xuất tất cả người dùng (Fetch All Users)
- **Endpoint**: `/fetch_all_users`
- **Phương thức**: GET
- **Mô tả**: Truy xuất tất cả người dùng từ cơ sở dữ liệu.
- **Phản hồi**:
  - `users` (list): Danh sách tất cả người dùng.

### 7. Truy xuất email dựa trên tên người dùng (Fetch Emails by User)
- **Endpoint**: `/fetch_emails_by_user`
- **Phương thức**: GET
- **Mô tả**: Truy xuất email dựa trên tên người dùng.
- **Yêu cầu**:
  - `username` (str): Tên người dùng.
- **Phản hồi**:
  - `emails` (list): Danh sách email của người dùng.

```json
{
  "username": "example_user"
}
```

### 8. Làm mới danh sách email (Refresh Emails)
- **Endpoint**: `/refresh_emails`
- **Phương thức**: GET
- **Mô tả**: Làm mới danh sách email.
- **Phản hồi**:
  - `emails` (list): Danh sách email đã làm mới.

## Nguyên tắc thiết kế
- **Tách biệt mối quan tâm (Separation of Concerns - SoC)**: Tách biệt rõ ràng giữa lớp trình diễn và lớp logic kinh doanh.
- **Nguyên tắc đơn nhiệm (Single Responsibility Principle - SRP)**: Mỗi lớp chỉ thực hiện một nhiệm vụ duy nhất.
- **Nguyên tắc đảo ngược phụ thuộc (Dependency Inversion Principle - DIP)**: Sử dụng các giao diện và các lớp trừu tượng để giảm thiểu sự phụ thuộc.
- **Mẫu thiết kế MVC (Model-View-Controller)**: Áp dụng mẫu thiết kế MVC để tách biệt rõ ràng giữa các lớp.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của các API trong hệ thống mailServer.
