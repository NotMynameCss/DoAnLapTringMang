# Use Case: Xóa email

## Mô tả
Người dùng có thể xóa email.

## Các bước thực hiện
1. Người dùng mở giao diện danh sách email.
2. Người dùng chọn email cần xóa.
3. Người dùng nhấn nút "Xóa".
4. Hệ thống kiểm tra thông tin email.
5. Nếu thông tin email hợp lệ, hệ thống xóa email khỏi cơ sở dữ liệu.
6. Nếu thông tin email không hợp lệ, hệ thống hiển thị thông báo lỗi.

## Sơ đồ Use Case

```plaintext
+----------------+       +----------------+       +----------------+
|    Người dùng  |       |    Hệ thống    |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Mở giao diện danh    |                        |
        |   sách email           |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Chọn email cần xóa   |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Nhấn nút "Xóa"       |                        |
        |----------------------->|                        |
        |                        |   Kiểm tra thông tin   |
        |                        |   email                |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Thông tin hợp lệ     |
        |                        |<-----------------------|
        |                        |                        |
        |   Xóa email khỏi CSDL  |                        |
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
Use case "Xóa email" giúp xác định các bước cần thiết để người dùng có thể xóa email trên hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
