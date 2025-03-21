# Phân tích và thiết kế hệ thống mail sử dụng TCP/IP

## Tổng quan
Hệ thống mail sử dụng giao thức TCP/IP để truyền tải dữ liệu giữa máy chủ và máy khách. Hệ thống này tuân theo mô hình MVC (Model-View-Controller) để tách biệt các thành phần giao diện, logic nghiệp vụ và dữ liệu.

## Kiến trúc hệ thống

### 1. Giao thức TCP/IP
- **TCP/IP** (Transmission Control Protocol/Internet Protocol) là một bộ giao thức truyền thông được sử dụng để kết nối các thiết bị mạng trên Internet.
- **TCP** đảm bảo dữ liệu được truyền tải một cách đáng tin cậy và theo thứ tự.
- **IP** chịu trách nhiệm định tuyến các gói dữ liệu đến đúng địa chỉ đích.

### 2. Mô hình MVC
- **Model**: Quản lý dữ liệu và logic nghiệp vụ của ứng dụng.
- **View**: Quản lý giao diện người dùng và hiển thị dữ liệu.
- **Controller**: Xử lý các yêu cầu từ người dùng, tương tác với Model và cập nhật View.

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

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của hệ thống mail sử dụng TCP/IP.
