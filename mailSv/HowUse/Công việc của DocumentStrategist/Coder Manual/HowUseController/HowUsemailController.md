# Hướng dẫn sử dụng `mailController` trong thư mục `mailSv`

## Tổng quan
`mailController` chịu trách nhiệm quản lý các hoạt động liên quan đến email như gửi email, truy xuất email, và xóa email.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **Giao thức TCP/IP**: Kết nối client-server qua cổng `65432`.
- **Loguru 0.7.3**: Ghi log chi tiết.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu trước khi lưu vào cơ sở dữ liệu.

## Các phương thức chính

### 1. `send_email`
- **Chức năng**: Gửi email và lưu thông tin vào cơ sở dữ liệu.
- **Cách sử dụng**:
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

### 2. `fetch_emails`
- **Chức năng**: Truy xuất email dựa trên loại email (inbox, sent).
- **Cách sử dụng**:
```python
emails = mail_controller.fetch_emails(email_type="inbox")
print(emails)
```

### 3. `delete_email`
- **Chức năng**: Xóa email của người dùng.
- **Cách sử dụng**:
```python
response = mail_controller.delete_email(email_id=123, user_id="example_user")
print(response)
```

### 4. `refresh_emails`
- **Chức năng**: Làm mới danh sách email.
- **Cách sử dụng**:
```python
mail_controller.refresh_emails()
```

## Cải tiến mới
- **Decorator `retry_with_limit`**: Giới hạn số lần thử lại khi xảy ra lỗi.
- **Connection Pooling**: Kích hoạt Connection Pooling trong SQLAlchemy để cải thiện hiệu suất.
- **Xử lý lỗi TCP**: Thêm cơ chế timeout và acknowledgment (ACK) để đảm bảo tính ổn định.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của `mailController` trong thư mục `mailSv`.
