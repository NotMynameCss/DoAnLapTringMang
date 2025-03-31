# API Documentation

## Tổng quan
API Documentation cung cấp thông tin chi tiết về các API được sử dụng trong hệ thống mailServer. Các API này chịu trách nhiệm xử lý các yêu cầu từ client và tương tác với cơ sở dữ liệu.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **Giao thức TCP/IP**: Kết nối client-server qua cổng `65432`.
- **Loguru 0.7.3**: Ghi log chi tiết.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu trước khi lưu vào cơ sở dữ liệu.
- **twisted 24.11.0**: Xử lý kết nối mạng không đồng bộ.

## Cải tiến mới
- **Cổng mới**: Hệ thống sử dụng cổng `65432` để giao tiếp giữa client và server.
- **Xác thực dữ liệu**: Sử dụng `pydantic` để validate dữ liệu trước khi lưu vào cơ sở dữ liệu, giảm thiểu lỗi dữ liệu không hợp lệ.
- **Xử lý lỗi TCP**: Thêm cơ chế quản lý timeout và xử lý lỗi TCP thông minh.

...existing API endpoints...
