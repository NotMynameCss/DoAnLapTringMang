# Bước 6: Thiết kế cơ sở dữ liệu

## Tổng quan
Thiết kế cơ sở dữ liệu là bước quan trọng để đảm bảo rằng dữ liệu được lưu trữ và truy xuất một cách hiệu quả. Mục tiêu của bước này là thiết kế các bảng dữ liệu một cách tối ưu và hoàn chỉnh cho hệ thống mailServer.

## Các bảng dữ liệu chính

### 1. Bảng `users`
- **Chức năng**: Lưu trữ thông tin người dùng.
- **Cấu trúc**:
  - `id` (Integer, Primary Key, Auto Increment): Mã định danh duy nhất cho mỗi người dùng.
  - `username` (String, Unique, Not Null): Tên đăng nhập của người dùng.
  - `password` (String, Not Null): Mật khẩu của người dùng.

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

### 2. Bảng `emails`
- **Chức năng**: Lưu trữ thông tin email.
- **Cấu trúc**:
  - `id` (Integer, Primary Key, Auto Increment): Mã định danh duy nhất cho mỗi email.
  - `sender` (String, Not Null): Địa chỉ email của người gửi.
  - `recipients` (Text, Not Null): Danh sách địa chỉ email của người nhận.
  - `cc` (Text): Danh sách địa chỉ email của người nhận CC.
  - `bcc` (Text): Danh sách địa chỉ email của người nhận BCC.
  - `subject` (String): Chủ đề của email.
  - `body` (Text): Nội dung của email.
  - `attachments` (Text): Danh sách tệp đính kèm.
  - `timestamp` (TIMESTAMP, Default Current Timestamp): Thời gian gửi email.

```sql
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
```

### 3. Bảng `labels`
- **Chức năng**: Lưu trữ thông tin nhãn.
- **Cấu trúc**:
  - `id` (Integer, Primary Key, Auto Increment): Mã định danh duy nhất cho mỗi nhãn.
  - `name` (String, Not Null): Tên của nhãn.
  - `user_id` (Integer, Foreign Key): Mã định danh của người dùng tạo nhãn.

```sql
CREATE TABLE labels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 4. Bảng `email_labels`
- **Chức năng**: Lưu trữ mối quan hệ giữa email và nhãn.
- **Cấu trúc**:
  - `email_id` (Integer, Foreign Key): Mã định danh của email.
  - `label_id` (Integer, Foreign Key): Mã định danh của nhãn.

```sql
CREATE TABLE email_labels (
    email_id INT,
    label_id INT,
    FOREIGN KEY (email_id) REFERENCES emails(id),
    FOREIGN KEY (label_id) REFERENCES labels(id)
);
```

## Kết luận
Thiết kế cơ sở dữ liệu giúp xác định cấu trúc và mối quan hệ giữa các bảng dữ liệu trong hệ thống mailServer. Điều này giúp đảm bảo rằng dữ liệu được lưu trữ và truy xuất một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
