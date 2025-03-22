# Use Case: Gửi email

## Mô tả
Người dùng có thể gửi email đến người nhận.

## Các bước thực hiện
1. Người dùng mở giao diện soạn email.
2. Người dùng nhập thông tin người nhận, chủ đề và nội dung email.
3. Người dùng nhấn nút "Gửi".
4. Hệ thống kiểm tra thông tin email.
5. Nếu thông tin email hợp lệ, hệ thống gửi email và lưu vào cơ sở dữ liệu.
6. Nếu thông tin email không hợp lệ, hệ thống hiển thị thông báo lỗi.

## Sơ đồ Use Case

```plaintext
+----------------+       +----------------+       +----------------+
|    Người dùng  |       |    Hệ thống    |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Mở giao diện soạn    |                        |
        |   email                |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Nhập thông tin       |                        |
        |   người nhận, chủ đề   |                        |
        |   và nội dung email    |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Nhấn nút "Gửi"       |                        |
        |----------------------->|                        |
        |                        |   Kiểm tra thông tin   |
        |                        |   email                |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Thông tin hợp lệ     |
        |                        |<-----------------------|
        |                        |                        |
        |   Gửi email và lưu     |                        |
        |   vào CSDL             |                        |
        |<-----------------------|                        |
        |                        |                        |
        |                        |   Thông tin không hợp lệ|
        |                        |<-----------------------|
        |                        |                        |
        |   Hiển thị thông báo   |                        |
        |   lỗi                  |                        |
        |<-----------------------|                        |
        |                        |                        |
```

## Kết luận
Use case "Gửi email" giúp xác định các bước cần thiết để người dùng có thể gửi email đến người nhận trên hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
