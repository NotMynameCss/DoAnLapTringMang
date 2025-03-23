# Hướng dẫn sử dụng `authController` trong thư mục `mailSv`

## Tổng quan
`authController` chịu trách nhiệm quản lý xác thực người dùng, bao gồm đăng nhập và đăng ký.

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

### 1. `login`
- **Chức năng**: Kiểm tra thông tin đăng nhập và trả về kết quả.
- **Cách sử dụng**:
```python
response = auth_controller.login(username="username", password="password")
print(response)
```

### 2. `register`
- **Chức năng**: Đăng ký người dùng mới và lưu thông tin vào cơ sở dữ liệu.
- **Cách sử dụng**:
```python
response = auth_controller.register(username="username", password="password")
print(response)
```

### 3. `verify_table_exists`
- **Chức năng**: Kiểm tra và tạo bảng `users` nếu chưa tồn tại trong cơ sở dữ liệu.
- **Cách sử dụng**:
```python
auth_controller.verify_table_exists()
```

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của `authController` trong thư mục `mailSv`.
