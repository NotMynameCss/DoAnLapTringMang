# Bước 2: Phân tích hệ thống mailServer

## Tổng quan
Phân tích hệ thống là bước tiếp theo sau khi thu thập và phân tích yêu cầu. Mục tiêu của bước này là xác định các thành phần chính của hệ thống và cách chúng tương tác với nhau.

## Các thành phần chính

### 1. Máy chủ (Server)
- **Chức năng**: Xử lý các yêu cầu từ máy khách, quản lý dữ liệu và gửi phản hồi lại cho máy khách.
- **Thành phần**:
  - **Socket Server**: Lắng nghe các kết nối từ máy khách và tạo luồng mới để xử lý từng kết nối.
  - **Controller**: Xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu.
  - **Model**: Quản lý dữ liệu và thực hiện các thao tác CRUD trên cơ sở dữ liệu.

### 2. Máy khách (Client)
- **Chức năng**: Gửi yêu cầu đến máy chủ và hiển thị dữ liệu nhận được từ máy chủ.
- **Thành phần**:
  - **Socket Client**: Kết nối đến máy chủ và gửi/nhận dữ liệu.
  - **View**: Quản lý giao diện người dùng và hiển thị dữ liệu.
  - **Controller**: Xử lý các yêu cầu từ người dùng và gửi yêu cầu đến máy chủ.

## Quy trình hoạt động

### 1. Khởi động máy chủ
- Máy chủ tạo một socket và lắng nghe các kết nối từ máy khách trên một cổng cụ thể.
- Khi nhận được kết nối từ máy khách, máy chủ tạo một luồng mới để xử lý kết nối đó.

### 2. Đăng nhập/Đăng ký
- Máy khách gửi yêu cầu đăng nhập hoặc đăng ký đến máy chủ.
- Máy chủ nhận yêu cầu, kiểm tra thông tin người dùng trong cơ sở dữ liệu và gửi phản hồi lại cho máy khách.

### 3. Gửi email
- Máy khách gửi yêu cầu gửi email đến máy chủ.
- Máy chủ nhận yêu cầu, lưu thông tin email vào cơ sở dữ liệu và gửi phản hồi lại cho máy khách.

### 4. Truy xuất email
- Máy khách gửi yêu cầu truy xuất email đến máy chủ.
- Máy chủ nhận yêu cầu, truy vấn cơ sở dữ liệu và gửi danh sách email lại cho máy khách.

## Lưu đồ hoạt động

```plaintext
+----------------+       +----------------+       +----------------+
|    Máy khách   |       |    Máy chủ     |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Kết nối đến máy chủ  |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Gửi yêu cầu đăng nhập|                        |
        |----------------------->|                        |
        |                        |   Kiểm tra thông tin   |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi phản hồi đăng nhập|
        |<-----------------------|                        |
        |                        |                        |
        |   Gửi yêu cầu gửi email|                        |
        |----------------------->|                        |
        |                        |   Lưu email vào CSDL   |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi phản hồi gửi email|
        |<-----------------------|                        |
        |                        |                        |
        |   Gửi yêu cầu truy xuất email                   |
        |----------------------->|                        |
        |                        |   Truy vấn email từ CSDL|
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi danh sách email  |
        |<-----------------------|                        |
        |                        |                        |
```

## Kết luận
Phân tích hệ thống giúp xác định các thành phần chính và quy trình hoạt động của hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
