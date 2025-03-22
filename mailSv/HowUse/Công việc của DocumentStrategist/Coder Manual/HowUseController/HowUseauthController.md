# Hướng dẫn sử dụng `authController` trong thư mục `mailSv`

## Tổng quan
`authController` chịu trách nhiệm quản lý xác thực người dùng, bao gồm đăng nhập và đăng ký.

## Công nghệ sử dụng
- **Python 3.11.9**: Ngôn ngữ lập trình chính.
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

## Nguyên tắc thiết kế
- **Tách biệt mối quan tâm (Separation of Concerns - SoC)**: Tách biệt rõ ràng giữa lớp trình diễn và lớp logic kinh doanh.
- **Nguyên tắc đơn nhiệm (Single Responsibility Principle - SRP)**: Mỗi lớp chỉ thực hiện một nhiệm vụ duy nhất.
- **Nguyên tắc đảo ngược phụ thuộc (Dependency Inversion Principle - DIP)**: Sử dụng các giao diện và các lớp trừu tượng để giảm thiểu sự phụ thuộc.
- **Mẫu thiết kế MVC (Model-View-Controller)**: Áp dụng mẫu thiết kế MVC để tách biệt rõ ràng giữa các lớp.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của `authController` trong thư mục `mailSv`.
