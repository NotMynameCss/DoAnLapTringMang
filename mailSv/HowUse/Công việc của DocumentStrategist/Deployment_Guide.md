# Hướng dẫn triển khai hệ thống mailServer

## Tổng quan
Hướng dẫn này cung cấp các bước chi tiết để triển khai hệ thống mailServer. Hệ thống được xây dựng bằng Python và sử dụng các công nghệ như XAMPP, Tkinter, và giao thức TCP/IP.

## Công nghệ sử dụng
- **Python 3.11.9**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **Giao thức TCP/IP**: Kết nối client-server.
- **Tkinter**: Xây dựng giao diện người dùng.
- **Loguru 0.7.3**: Ghi log.
- **SqlAlchemy 2.0.39**: ORM để tương tác với cơ sở dữ liệu.
- **pydantic 2.10.6**: Xác thực dữ liệu.
- **twisted 24.11.0**: Xử lý kết nối mạng không đồng bộ.

## Các bước triển khai

### 1. Chuẩn bị môi trường
- **Cài đặt Python 3.11.9**:
  - Tải Python từ trang chủ [python.org](https://www.python.org/downloads/release/python-3119/).
  - Chạy file cài đặt và làm theo hướng dẫn để cài đặt Python.

- **Cài đặt XAMPP**:
  - Tải XAMPP từ trang chủ [apachefriends.org](https://www.apachefriends.org/download.html).
  - Chạy file cài đặt và làm theo hướng dẫn để cài đặt XAMPP.

- **Cài đặt các thư viện cần thiết**:
  - Mở Command Prompt và chạy các lệnh sau để cài đặt các thư viện:
    ```sh
    pip install loguru==0.7.3
    pip install sqlalchemy==2.0.39
    pip install pydantic==2.10.6
    pip install twisted==24.11.0
    ```

### 2. Cài đặt và cấu hình cơ sở dữ liệu
- **Khởi động XAMPP**:
  - Mở XAMPP Control Panel và khởi động Apache và MySQL.

- **Tạo cơ sở dữ liệu MySQL**:
  - Mở phpMyAdmin từ XAMPP Control Panel.
  - Tạo cơ sở dữ liệu mới với tên `mailserver`.

- **Tạo các bảng trong cơ sở dữ liệu**:
  - Chạy các lệnh SQL sau trong phpMyAdmin để tạo các bảng `users`, `emails`, `labels`, và `email_labels`:
    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );

    CREATE TABLE emails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sender VARCHAR(255) NOT NULL,
        recipients TEXT NOT NULL,
        cc TEXT,
        bcc TEXT,
        subject VARCHAR(255),
        body TEXT,
        attachments TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE labels (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE email_labels (
        email_id INT,
        label_id INT,
        FOREIGN KEY (email_id) REFERENCES emails(id),
        FOREIGN KEY (label_id) REFERENCES labels(id)
    );
    ```

### 3. Triển khai máy chủ (Server)
- **Cấu hình máy chủ**:
  - Tạo một file Python mới `server.py` và cấu hình máy chủ để lắng nghe các kết nối từ máy khách.
  - Sử dụng `twisted` để xử lý kết nối mạng không đồng bộ.

- **Triển khai các thành phần chính của máy chủ**:
  - Tạo các file Python cho `Socket Server`, `Controller`, và `Model`.
  - Đảm bảo rằng các thành phần này tương tác đúng với cơ sở dữ liệu và xử lý các yêu cầu từ máy khách.

### 4. Triển khai máy khách (Client)
- **Cấu hình máy khách**:
  - Tạo một file Python mới `client.py` và cấu hình máy khách để kết nối đến máy chủ.
  - Sử dụng `Tkinter` để xây dựng giao diện người dùng.

- **Triển khai các thành phần chính của máy khách**:
  - Tạo các file Python cho `Socket Client`, `View`, và `Controller`.
  - Đảm bảo rằng các thành phần này tương tác đúng với máy chủ và hiển thị dữ liệu cho người dùng.

### 5. Kiểm thử hệ thống
- **Kiểm thử chức năng**:
  - Thực hiện kiểm thử các chức năng chính như đăng nhập, đăng ký, gửi email, và truy xuất email để đảm bảo rằng hệ thống hoạt động đúng theo yêu cầu.

- **Kiểm thử hiệu suất**:
  - Thực hiện kiểm thử hiệu suất để đảm bảo rằng hệ thống đáp ứng được các yêu cầu về hiệu suất.

### 6. Triển khai hệ thống
- **Triển khai lên môi trường sản xuất**:
  - Triển khai hệ thống mailServer lên môi trường sản xuất.
  - Đảm bảo rằng hệ thống hoạt động ổn định và đáp ứng được các yêu cầu của người dùng.

## Kết luận
Hướng dẫn triển khai này giúp xác định các bước cần thiết để triển khai hệ thống mailServer một cách hiệu quả. Điều này giúp đảm bảo rằng hệ thống được triển khai đúng theo kế hoạch và đáp ứng được các yêu cầu của người dùng.
