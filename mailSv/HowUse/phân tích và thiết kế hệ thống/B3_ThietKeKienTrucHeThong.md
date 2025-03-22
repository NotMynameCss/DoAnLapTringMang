# Bước 3: Thiết kế kiến trúc hệ thống

## Tổng quan
Thiết kế kiến trúc hệ thống là bước tiếp theo sau khi phân tích hệ thống. Mục tiêu của bước này là xác định kiến trúc tổng thể của hệ thống mailServer, bao gồm các thành phần chính và cách chúng tương tác với nhau.

## Kiến trúc hệ thống

### 1. Mô hình MVC (Model-View-Controller)
- **Model**: Quản lý dữ liệu và logic nghiệp vụ của ứng dụng.
- **View**: Quản lý giao diện người dùng và hiển thị dữ liệu.
- **Controller**: Xử lý các yêu cầu từ người dùng, tương tác với Model và cập nhật View.

### 2. Kiến trúc Client-Server
- **Client**: Gửi yêu cầu đến máy chủ và hiển thị dữ liệu nhận được từ máy chủ.
- **Server**: Xử lý các yêu cầu từ máy khách, quản lý dữ liệu và gửi phản hồi lại cho máy khách.

## Các thành phần chính

### 1. Máy chủ (Server)
- **Socket Server**: Lắng nghe các kết nối từ máy khách và tạo luồng mới để xử lý từng kết nối.
- **Controller**: Xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu.
- **Model**: Quản lý dữ liệu và thực hiện các thao tác CRUD trên cơ sở dữ liệu.

### 2. Máy khách (Client)
- **Socket Client**: Kết nối đến máy chủ và gửi/nhận dữ liệu.
- **View**: Quản lý giao diện người dùng và hiển thị dữ liệu.
- **Controller**: Xử lý các yêu cầu từ người dùng và gửi yêu cầu đến máy chủ.

## Sơ đồ kiến trúc hệ thống

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
Thiết kế kiến trúc hệ thống giúp xác định cấu trúc tổng thể của hệ thống mailServer và cách các thành phần chính tương tác với nhau. Điều này giúp đảm bảo rằng hệ thống được thiết kế một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
