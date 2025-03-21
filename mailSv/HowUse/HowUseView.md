# Hướng dẫn sử dụng giao diện trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần giao diện của ứng dụng Mail Server. Giao diện được xây dựng bằng thư viện Tkinter của Python và tuân theo mô hình MVC (Model-View-Controller).

## Các thành phần chính

### 1. `mainView.py`
- Đây là giao diện chính của ứng dụng Mail Server.
- Khi khởi động, nó sẽ hiển thị màn hình đăng nhập/đăng ký (`AuthView`).

### 2. `authView.py`
- Giao diện đăng nhập và đăng ký người dùng.
- Người dùng có thể nhập tài khoản và mật khẩu để đăng nhập hoặc đăng ký.
- Sau khi đăng nhập thành công, giao diện sẽ chuyển sang `MailView`.

### 3. `mailView.py`
- Giao diện chính sau khi người dùng đăng nhập thành công.
- Bao gồm các thành phần:
  - **Khung chính** (`main_frame`): Chứa toàn bộ giao diện.
  - **Khung trên cùng** (`top_frame`): Chứa thanh tìm kiếm và nút soạn thư mới.
  - **Khung bên trái** (`left_frame`): Chứa các nút điều hướng như Hộp thư đến, Đã gửi, Thư nháp, Thùng rác, Nhãn.
  - **Khung bên phải** (`right_frame`): Hiển thị danh sách người dùng và chi tiết người dùng.
  - **Khung dưới cùng** (`bottom_frame`): Chứa các nút cài đặt và Chat/Meet.

### 4. `mailSendView.py`
- Giao diện soạn email mới.
- Người dùng có thể nhập thông tin người nhận, tiêu đề, nội dung và đính kèm tệp.

## Chi tiết giao diện `mailView.py`

### Khung chính (`main_frame`)
- Chứa toàn bộ giao diện của `MailView`.
- Được tạo bằng `tk.Frame` và đặt nền màu trắng.

### Khung trên cùng (`top_frame`)
- Chứa thanh tìm kiếm và nút soạn thư mới.
- Các thành phần:
  - **Nút Soạn Thư** (`compose_button`): Khi nhấn vào, sẽ gọi hàm `compose_email` để mở giao diện soạn email mới.
  - **Ô tìm kiếm** (`search_entry`): Người dùng có thể nhập từ khóa để tìm kiếm email.
  - **Nút Tìm Kiếm** (`search_button`): Khi nhấn vào, sẽ gọi hàm `search_email` để thực hiện tìm kiếm email.
  - **Nút Làm mới** (`refresh_button`): Khi nhấn vào, sẽ gọi hàm `show_users` để hiển thị danh sách người dùng.

### Khung bên trái (`left_frame`)
- Chứa các nút điều hướng như Hộp thư đến, Đã gửi, Thư nháp, Thùng rác, Nhãn.
- Các thành phần:
  - **Nút Hộp thư đến** (`inbox_button`): Khi nhấn vào, sẽ gọi hàm `show_inbox` để hiển thị hộp thư đến.
  - **Nút Đã gửi** (`sent_button`): Khi nhấn vào, sẽ gọi hàm `show_sent` để hiển thị thư đã gửi.
  - **Nút Thư nháp** (`drafts_button`): Khi nhấn vào, sẽ gọi hàm `show_drafts` để hiển thị thư nháp.
  - **Nút Thùng rác** (`trash_button`): Khi nhấn vào, sẽ gọi hàm `show_trash` để hiển thị thùng rác.
  - **Nút Nhãn** (`labels_button`): Khi nhấn vào, sẽ gọi hàm `show_labels` để hiển thị nhãn.

### Khung bên phải (`right_frame`)
- Hiển thị danh sách người dùng và chi tiết người dùng.
- Các thành phần:
  - **Danh sách người dùng** (`user_listbox`): Hiển thị danh sách tất cả người dùng từ cơ sở dữ liệu.
  - **Chi tiết người dùng** (`user_details_tree`): Hiển thị chi tiết thông tin người dùng khi được chọn từ danh sách.

### Khung dưới cùng (`bottom_frame`)
- Chứa các nút cài đặt và Chat/Meet.
- Các thành phần:
  - **Nút Cài đặt** (`settings_button`): Khi nhấn vào, sẽ gọi hàm `show_settings` để hiển thị cài đặt.
  - **Nút Chat/Meet** (`chat_button`): Khi nhấn vào, sẽ gọi hàm `show_chat` để hiển thị chức năng Chat/Meet.

## Cách hoạt động

1. **Khởi động ứng dụng**:
   - Khi khởi động, `mainView.py` sẽ hiển thị giao diện đăng nhập/đăng ký (`AuthView`).

2. **Đăng nhập/Đăng ký**:
   - Người dùng nhập tài khoản và mật khẩu, sau đó nhấn nút Đăng nhập hoặc Đăng ký.
   - Nếu đăng nhập thành công, giao diện sẽ chuyển sang `MailView`.

3. **Giao diện chính (`MailView`)**:
   - Người dùng có thể sử dụng các nút điều hướng để xem hộp thư đến, thư đã gửi, thư nháp, thùng rác và nhãn.
   - Có thể tìm kiếm email bằng cách nhập từ khóa vào thanh tìm kiếm và nhấn nút Tìm Kiếm.
   - Nhấn nút Soạn Thư để mở giao diện soạn email mới (`MailSendView`).
   - Nhấn nút Làm mới để hiển thị danh sách người dùng từ cơ sở dữ liệu.

4. **Soạn email mới (`MailSendView`)**:
   - Người dùng nhập thông tin người nhận, tiêu đề, nội dung và có thể đính kèm tệp.
   - Nhấn nút Gửi để gửi email hoặc Lưu nháp để lưu email vào thư nháp.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của giao diện trong thư mục `mailSv`.
