# Use Case: Đăng nhập

## Mô tả
Người dùng có thể đăng nhập vào hệ thống bằng tài khoản đã đăng ký.

## Các bước thực hiện
1. Người dùng mở ứng dụng và nhập tên đăng nhập và mật khẩu.
2. Người dùng nhấn nút "Đăng nhập".
3. Hệ thống kiểm tra thông tin đăng nhập.
4. Nếu thông tin đăng nhập hợp lệ, hệ thống cho phép người dùng truy cập vào giao diện chính.
5. Nếu thông tin đăng nhập không hợp lệ, hệ thống hiển thị thông báo lỗi.

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
        |   Nhấn nút "Đăng nhập" |                        |
        |----------------------->|                        |
        |                        |   Kiểm tra thông tin   |
        |                        |   đăng nhập            |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Thông tin hợp lệ     |
        |                        |<-----------------------|
        |                        |                        |
        |   Truy cập giao diện   |                        |
        |   chính                |                        |
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
Use case "Đăng nhập" giúp xác định các bước cần thiết để người dùng có thể đăng nhập vào hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
