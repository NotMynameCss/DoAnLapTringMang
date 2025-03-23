# README

## Tổng quan
Dự án `mailSv` và `mailClient` là một hệ thống Mail Server-Client được xây dựng bằng Python, sử dụng giao thức TCP/IP để kết nối giữa client và server. Hệ thống tuân theo mô hình MVC (Model-View-Controller) để tách biệt các thành phần giao diện, logic nghiệp vụ và dữ liệu.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **Giao thức TCP/IP**: Kết nối client-server.
- **Tkinter**: Xây dựng giao diện người dùng.
- **Loguru 0.7.3**: Ghi log.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu.
- **twisted 24.11.0**: Xử lý kết nối mạng không đồng bộ.

## Các thay đổi mới nhất so với phiên bản V.0.2.3.1

### mailSv

1. **Cập nhật `authController`**:
   - Thêm xác thực dữ liệu bằng `pydantic`.
   - Cải thiện xử lý lỗi và ghi log.

2. **Cập nhật `mailController`**:
   - Tách biệt các chức năng gửi email, truy xuất email và tìm kiếm email thành các controller riêng (`fetchMailController`, `sendMailController`, `searchMailController`).
   - Thêm phương thức `fetch_email_details` để truy xuất chi tiết email.

3. **Cập nhật `dbconnector.py`**:
   - Thêm các chỉ mục (index) để tối ưu hóa truy vấn cơ sở dữ liệu.
   - Cải thiện kết nối cơ sở dữ liệu và xử lý lỗi.

4. **Cập nhật `server.py`**:
   - Thêm xử lý các lệnh mới từ client như `FETCH_ALL_EMAILS`, `FETCH_ALL_USERS`, `REFRESH_EMAILS`.
   - Sử dụng `pydantic` để xác thực dữ liệu nhận từ client.

5. **Cập nhật giao diện `mailView`**:
   - Thêm chức năng soạn email mới (`MailSendView`).
   - Cải thiện giao diện người dùng và xử lý sự kiện.

### mailClient

1. **Cập nhật `authController`**:
   - Thêm xác thực dữ liệu bằng `pydantic`.
   - Cải thiện xử lý lỗi và ghi log.

2. **Cập nhật `mailController`**:
   - Thêm phương thức `send_email` để gửi email từ client đến server.
   - Thêm phương thức `fetch_emails` và `fetch_all_emails` để truy xuất email từ server.

3. **Cập nhật giao diện `authView`**:
   - Cải thiện giao diện đăng nhập và đăng ký người dùng.
   - Thêm xử lý sự kiện và thông báo lỗi.

4. **Cập nhật giao diện `mailView`**:
   - Thêm chức năng soạn email mới (`MailSendView`).
   - Cải thiện giao diện người dùng và xử lý sự kiện.

## Hướng dẫn triển khai

### Chuẩn bị môi trường
- Cài đặt Python 3.13.2 trên máy chủ và máy khách.
- Cài đặt XAMPP (xampp-windows-x64-8.2.12-0) để quản lý cơ sở dữ liệu.
- Cài đặt các thư viện cần thiết:
  ```sh
  pip install loguru==0.7.3
  pip install sqlalchemy==2.0.39
  pip install pydantic==2.10.6
  pip install twisted==24.11.0
  ```

### Cài đặt và cấu hình cơ sở dữ liệu
- Khởi động XAMPP và tạo cơ sở dữ liệu MySQL với tên `mailserver`.
- Tạo các bảng `users`, `emails`, `labels`, và `email_labels` trong cơ sở dữ liệu.

### Triển khai máy chủ (Server)
- Cấu hình và triển khai các thành phần chính của máy chủ: `Socket Server`, `Controller`, `Model`.

### Triển khai máy khách (Client)
- Cấu hình và triển khai các thành phần chính của máy khách: `Socket Client`, `View`, `Controller`.

### Kiểm thử hệ thống
- Thực hiện kiểm thử chức năng và hiệu suất để đảm bảo hệ thống hoạt động đúng theo yêu cầu.

### Triển khai hệ thống
- Triển khai hệ thống mailServer lên môi trường sản xuất và đảm bảo hệ thống hoạt động ổn định.

## Kết luận
Các thay đổi mới nhất giúp cải thiện hiệu suất, bảo mật và khả năng sử dụng của hệ thống mailServer và mailClient. Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách triển khai và sử dụng hệ thống.

