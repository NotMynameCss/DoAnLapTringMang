# Bước 7: Thiết kế chi tiết luồng giao tiếp dữ liệu

## Tổng quan
Thiết kế chi tiết luồng giao tiếp dữ liệu là bước quan trọng để đảm bảo rằng dữ liệu được truyền tải một cách hiệu quả giữa các thành phần của hệ thống mailServer. Mục tiêu của bước này là xác định chi tiết các luồng giao tiếp dữ liệu giữa client và server.

## Các thành phần chính

### 1. Máy chủ (Server)
- **Socket Server**: Lắng nghe các kết nối từ máy khách và tạo luồng mới để xử lý từng kết nối.
- **Controller**: Xử lý logic nghiệp vụ và tương tác với cơ sở dữ liệu.
- **Model**: Quản lý dữ liệu và thực hiện các thao tác CRUD trên cơ sở dữ liệu.

### 2. Máy khách (Client)
- **Socket Client**: Kết nối đến máy chủ và gửi/nhận dữ liệu.
- **View**: Quản lý giao diện người dùng và hiển thị dữ liệu.
- **Controller**: Xử lý các yêu cầu từ người dùng và gửi yêu cầu đến máy chủ.

## Luồng giao tiếp dữ liệu

### 1. Đăng nhập
- **Client**:
  - Người dùng nhập tên đăng nhập và mật khẩu.
  - Gửi yêu cầu đăng nhập đến máy chủ.
- **Server**:
  - Nhận yêu cầu đăng nhập.
  - Kiểm tra thông tin đăng nhập trong cơ sở dữ liệu.
  - Gửi phản hồi đăng nhập lại cho máy khách.

```plaintext
+----------------+       +----------------+       +----------------+
|    Máy khách   |       |    Máy chủ     |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Nhập tên đăng nhập   |                        |
        |   và mật khẩu          |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Gửi yêu cầu đăng nhập|                        |
        |----------------------->|                        |
        |                        |   Kiểm tra thông tin   |
        |                        |   đăng nhập            |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi phản hồi đăng nhập|
        |<-----------------------|                        |
        |                        |                        |
```

### 2. Gửi email
- **Client**:
  - Người dùng nhập thông tin email.
  - Gửi yêu cầu gửi email đến máy chủ.
- **Server**:
  - Nhận yêu cầu gửi email.
  - Lưu thông tin email vào cơ sở dữ liệu.
  - Gửi phản hồi gửi email lại cho máy khách.

```plaintext
+----------------+       +----------------+       +----------------+
|    Máy khách   |       |    Máy chủ     |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Nhập thông tin email |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Gửi yêu cầu gửi email|                        |
        |----------------------->|                        |
        |                        |   Lưu thông tin email  |
        |                        |   vào CSDL             |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi phản hồi gửi email|
        |<-----------------------|                        |
        |                        |                        |
```

### 3. Truy xuất email
- **Client**:
  - Người dùng gửi yêu cầu truy xuất email đến máy chủ.
- **Server**:
  - Nhận yêu cầu truy xuất email.
  - Truy vấn cơ sở dữ liệu và lấy danh sách email.
  - Gửi danh sách email lại cho máy khách.

```plaintext
+----------------+       +----------------+       +----------------+
|    Máy khách   |       |    Máy chủ     |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Gửi yêu cầu truy xuất|                        |
        |   email                |                        |
        |----------------------->|                        |
        |                        |   Truy vấn email từ    |
        |                        |   CSDL                 |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi danh sách email  |
        |<-----------------------|                        |
        |                        |                        |
```

### 4. Tìm kiếm email
- **Client**:
  - Người dùng nhập từ khóa tìm kiếm.
  - Gửi yêu cầu tìm kiếm email đến máy chủ.
- **Server**:
  - Nhận yêu cầu tìm kiếm email.
  - Truy vấn cơ sở dữ liệu và lấy danh sách email phù hợp.
  - Gửi danh sách email lại cho máy khách.

```plaintext
+----------------+       +----------------+       +----------------+
|    Máy khách   |       |    Máy chủ     |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Nhập từ khóa tìm     |                        |
        |   kiếm                 |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Gửi yêu cầu tìm kiếm |                        |
        |   email                |                        |
        |----------------------->|                        |
        |                        |   Truy vấn email từ    |
        |                        |   CSDL                 |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Gửi danh sách email  |
        |<-----------------------|                        |
        |                        |                        |
```

## Kết luận
Thiết kế chi tiết luồng giao tiếp dữ liệu giúp xác định cách dữ liệu được truyền tải giữa các thành phần của hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
