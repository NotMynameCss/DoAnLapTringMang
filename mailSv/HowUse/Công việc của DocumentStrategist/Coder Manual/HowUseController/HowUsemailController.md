# Hướng dẫn sử dụng `mailController` trong thư mục `mailSv`

## Tổng quan
`mailController` chịu trách nhiệm quản lý các hoạt động liên quan đến email như gửi email, truy xuất email và người dùng.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **Giao thức TCP/IP**: Kết nối client-server.
- **Loguru 0.7.3**: Ghi log.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu.
- **twisted 24.11.0**: Xử lý kết nối mạng không đồng bộ.

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
# Truy xuất email loại inbox
emails = mail_controller.fetch_emails("inbox")
print(emails)

# Truy xuất email loại sent
emails = mail_controller.fetch_emails("sent")
print(emails)
```

### 3. `fetch_all_emails`
- **Chức năng**: Truy xuất tất cả email từ cơ sở dữ liệu.
- **Cách sử dụng**:
```python
all_emails = mail_controller.fetch_all_emails()
print(all_emails)
```

### 4. `fetch_all_users`
- **Chức năng**: Truy xuất tất cả người dùng từ cơ sở dữ liệu.
- **Cách sử dụng**:
```python
all_users = mail_controller.fetch_all_users()
print(all_users)
```

### 5. `fetch_emails_by_user`
- **Chức năng**: Truy xuất email dựa trên tên người dùng.
- **Cách sử dụng**:
```python
user_emails = mail_controller.fetch_emails_by_user("username")
print(user_emails)
```

### 6. `refresh_emails`
- **Chức năng**: Làm mới danh sách email.
- **Cách sử dụng**:
```python
refreshed_emails = mail_controller.refresh_emails()
print(refreshed_emails)
```

## Nguyên tắc thiết kế
- **Tách biệt mối quan tâm (Separation of Concerns - SoC)**: Tách biệt rõ ràng giữa lớp trình diễn và lớp logic kinh doanh.
- **Nguyên tắc đơn nhiệm (Single Responsibility Principle - SRP)**: Mỗi lớp chỉ thực hiện một nhiệm vụ duy nhất.
- **Nguyên tắc đảo ngược phụ thuộc (Dependency Inversion Principle - DIP)**: Sử dụng các giao diện và các lớp trừu tượng để giảm thiểu sự phụ thuộc.
- **Mẫu thiết kế MVC (Model-View-Controller)**: Áp dụng mẫu thiết kế MVC để tách biệt rõ ràng giữa các lớp.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của `mailController` trong thư mục `mailSv`.
