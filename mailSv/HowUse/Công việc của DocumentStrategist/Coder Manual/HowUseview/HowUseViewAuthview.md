# Hướng dẫn sử dụng giao diện `authView` trong thư mục `mailSv`

## Tổng quan
Giao diện `authView` trong thư mục `mailSv` được sử dụng để đăng nhập và đăng ký người dùng. Giao diện này được xây dựng bằng thư viện Tkinter của Python và tuân theo mô hình MVC (Model-View-Controller).

## Các thành phần chính

### 1. `authView.py`
- Đây là giao diện chính của `authView`.
- Người dùng có thể nhập tài khoản và mật khẩu để đăng nhập hoặc đăng ký.
- Sau khi đăng nhập thành công, giao diện sẽ chuyển sang `MailView`.

### 2. `entryFrame.py`
- Khung nhập liệu cho tài khoản và mật khẩu.
- Bao gồm các thành phần:
  - **Nhãn tài khoản** (`username_label`): Hiển thị nhãn "tài khoản".
  - **Ô nhập tài khoản** (`username_entry`): Cho phép người dùng nhập tài khoản.
  - **Nhãn mật khẩu** (`password_label`): Hiển thị nhãn "Mật khẩu".
  - **Ô nhập mật khẩu** (`password_entry`): Cho phép người dùng nhập mật khẩu.
  - **Nhãn xác nhận mật khẩu** (`confirm_password_label`): Hiển thị nhãn "Nhập lại mật khẩu (Nếu đăng ký)".
  - **Ô nhập xác nhận mật khẩu** (`confirm_password_entry`): Cho phép người dùng nhập lại mật khẩu để xác nhận (chỉ sử dụng khi đăng ký).

### 3. `buttonFrame.py`
- Khung chứa các nút chức năng.
- Bao gồm các thành phần:
  - **Nút Đăng nhập** (`login_button`): Khi nhấn vào, sẽ gọi hàm `login` để thực hiện đăng nhập.
  - **Nút Đăng ký** (`register_button`): Khi nhấn vào, sẽ gọi hàm `register` để thực hiện đăng ký.

## Chi tiết giao diện `authView.py`

### Khởi tạo giao diện
- Khi khởi tạo, `AuthView` sẽ thiết lập các khung và các thành phần giao diện.
- Gọi hàm `show_auth` để hiển thị giao diện đăng nhập/đăng ký.

### Đăng nhập
- Khi nhấn nút Đăng nhập, hàm `login` sẽ được gọi.
- Hàm `login` sẽ lấy tài khoản và mật khẩu từ các ô nhập liệu và gửi yêu cầu đăng nhập đến `AuthController`.
- Nếu đăng nhập thành công, hàm `handle_login_response` sẽ được gọi để chuyển sang giao diện `MailView`.
- Nếu đăng nhập thất bại, một thông báo lỗi sẽ được hiển thị.

### Đăng ký
- Khi nhấn nút Đăng ký, hàm `register` sẽ được gọi.
- Hàm `register` sẽ lấy tài khoản và mật khẩu từ các ô nhập liệu và gửi yêu cầu đăng ký đến `AuthController`.
- Nếu đăng ký thành công, một thông báo thành công sẽ được hiển thị.
- Nếu đăng ký thất bại, một thông báo lỗi sẽ được hiển thị.

### Chi tiết các thành phần

#### `entryFrame.py`
- **Nhãn tài khoản** (`username_label`): Hiển thị nhãn "tài khoản".
- **Ô nhập tài khoản** (`username_entry`): Cho phép người dùng nhập tài khoản.
- **Nhãn mật khẩu** (`password_label`): Hiển thị nhãn "Mật khẩu".
- **Ô nhập mật khẩu** (`password_entry`): Cho phép người dùng nhập mật khẩu.
- **Nhãn xác nhận mật khẩu** (`confirm_password_label`): Hiển thị nhãn "Nhập lại mật khẩu (Nếu đăng ký)".
- **Ô nhập xác nhận mật khẩu** (`confirm_password_entry`): Cho phép người dùng nhập lại mật khẩu để xác nhận (chỉ sử dụng khi đăng ký).

#### `buttonFrame.py`
- **Nút Đăng nhập** (`login_button`): Khi nhấn vào, sẽ gọi hàm `login` để thực hiện đăng nhập.
- **Nút Đăng ký** (`register_button`): Khi nhấn vào, sẽ gọi hàm `register` để thực hiện đăng ký.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của giao diện `authView` trong thư mục `mailSv`.
