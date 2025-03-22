# Use Case: Tìm kiếm email

## Mô tả
Người dùng có thể tìm kiếm email dựa trên từ khóa.

## Các bước thực hiện
1. Người dùng mở giao diện tìm kiếm email.
2. Người dùng nhập từ khóa vào ô tìm kiếm.
3. Người dùng nhấn nút "Tìm Kiếm".
4. Hệ thống kiểm tra từ khóa và truy vấn cơ sở dữ liệu.
5. Hệ thống hiển thị danh sách email phù hợp với từ khóa.

## Sơ đồ Use Case

```plaintext
+----------------+       +----------------+       +----------------+
|    Người dùng  |       |    Hệ thống    |       |   Cơ sở dữ liệu |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |   Mở giao diện tìm     |                        |
        |   kiếm email           |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Nhập từ khóa vào ô   |                        |
        |   tìm kiếm             |                        |
        |----------------------->|                        |
        |                        |                        |
        |   Nhấn nút "Tìm Kiếm"  |                        |
        |----------------------->|                        |
        |                        |   Kiểm tra từ khóa và  |
        |                        |   truy vấn CSDL        |
        |                        |----------------------->|
        |                        |                        |
        |                        |   Danh sách email phù  |
        |                        |   hợp với từ khóa      |
        |                        |<-----------------------|
        |                        |                        |
        |   Hiển thị danh sách   |                        |
        |   email                |                        |
        |<-----------------------|                        |
        |                        |                        |
```

## Kết luận
Use case "Tìm kiếm email" giúp xác định các bước cần thiết để người dùng có thể tìm kiếm email dựa trên từ khóa trên hệ thống mailServer. Điều này giúp đảm bảo rằng hệ thống được thiết kế và triển khai một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
