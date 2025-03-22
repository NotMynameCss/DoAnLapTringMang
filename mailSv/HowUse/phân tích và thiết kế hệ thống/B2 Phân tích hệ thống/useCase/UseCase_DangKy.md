# Use Case: Đăng ký

## Mô tả
Người dùng có thể đăng ký tài khoản mới.

## Các bước thực hiện
1. Người dùng mở ứng dụng và nhập tên đăng nhập và mật khẩu.
2. Người dùng nhấn nút "Đăng ký".
3. Hệ thống kiểm tra thông tin đăng ký.
4. Nếu thông tin đăng ký hợp lệ, hệ thống tạo tài khoản mới và lưu vào cơ sở dữ liệu.
5. Nếu thông tin đăng ký không hợp lệ, hệ thống hiển thị thông báo lỗi.

## Sơ đồ Use Case

```plaintext
+----------------+       +----------------+       +----------------+
|    Người dùng  |       |    Hệ thống    |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Nhập tên đăng nhập   |                        |
        |   và mật khẩu          |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Nhấn nút "Đăng ký"   |                        |
        |----------------------->|                        |
        |                        |   Kiểm tra thông tin   |
        |                        |   đăng ký              |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Thông tin hợp lệ     |
        |                        |<-----------------------|
        |                        |                        |
        |   Tạo tài khoản mới    |                        |
        |   và lưu vào CSDL      |                        |
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
Use case "Đăng ký" giúp xác định các bước cần thiết để người dùng có thể đăng ký tài khoản mới trên hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
