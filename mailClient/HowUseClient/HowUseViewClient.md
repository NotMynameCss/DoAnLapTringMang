# Hướng dẫn sử dụng giao diện trong thư mục `mailClient`

## Tổng quan
Thư mục `mailClient` chứa các thành phần giao diện của ứng dụng Mail Client. Giao diện được xây dựng bằng thư viện Tkinter của Python và tuân theo mô hình MVC (Model-View-Controller).

## Các thành phần chính

### 1. `mainView.py`
- Đây là giao diện chính của ứng dụng Mail Client.
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
  - **Khung bên phải** (`right_frame`): Hiển thị danh sách email và chi tiết email.

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
  - **Nút Làm mới** (`refresh_button`): Khi nhấn vào, sẽ gọi hàm `refresh_emails` để làm mới danh sách email.

### Khung bên trái (`left_frame`)
- Chứa các nút điều hướng như Hộp thư đến, Đã gửi, Thư nháp, Thùng rác, Nhãn.
- Các thành phần:
  - **Nút Hộp thư đến** (`inbox_button`): Khi nhấn vào, sẽ gọi hàm `show_inbox` để hiển thị hộp thư đến.
  - **Nút Đã gửi** (`sent_button`): Khi nhấn vào, sẽ gọi hàm `show_sent` để hiển thị thư đã gửi.
  - **Nút Thư nháp** (`drafts_button`): Khi nhấn vào, sẽ gọi hàm `show_drafts` để hiển thị thư nháp.
  - **Nút Thùng rác** (`trash_button`): Khi nhấn vào, sẽ gọi hàm `show_trash` để hiển thị thùng rác.
  - **Nút Nhãn** (`labels_button`): Khi nhấn vào, sẽ gọi hàm `show_labels` để hiển thị nhãn.
  - **Nút Cài đặt** (`settings_button`): Khi nhấn vào, sẽ gọi hàm `show_settings` để hiển thị cài đặt.
  - **Nút Chat/Meet** (`chat_button`): Khi nhấn vào, sẽ gọi hàm `show_chat` để hiển thị chức năng Chat/Meet.

### Khung bên phải (`right_frame`)
- Hiển thị danh sách email và chi tiết email.
- Các thành phần:
  - **Danh sách email** (`email_details_tree`): Hiển thị danh sách tất cả email từ cơ sở dữ liệu.

### Cách hoạt động của `mailView.py`

1. **Khởi tạo giao diện**:
   - Khi khởi tạo, `MailView` sẽ thiết lập các khung và các thành phần giao diện.
   - Gọi hàm `show_emails` để hiển thị danh sách email từ cơ sở dữ liệu.

2. **Soạn email mới**:
   - Khi nhấn nút Soạn Thư, hàm `compose_email` sẽ được gọi để mở giao diện soạn email mới (`MailSendView`).

3. **Tìm kiếm email**:
   - Khi nhấn nút Tìm Kiếm, hàm `search_email` sẽ được gọi để tìm kiếm email dựa trên từ khóa nhập vào ô tìm kiếm.

4. **Hiển thị hộp thư đến**:
   - Khi nhấn nút Hộp thư đến, hàm `show_inbox` sẽ được gọi để hiển thị danh sách email trong hộp thư đến.

5. **Hiển thị thư đã gửi**:
   - Khi nhấn nút Đã gửi, hàm `show_sent` sẽ được gọi để hiển thị danh sách email đã gửi.

6. **Làm mới danh sách email**:
   - Khi nhấn nút Làm mới, hàm `refresh_emails` sẽ được gọi để làm mới danh sách email.

7. **Hiển thị danh sách email**:
   - Hàm `show_emails` sẽ được gọi khi khởi tạo giao diện để hiển thị danh sách email từ cơ sở dữ liệu.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của giao diện trong thư mục `mailClient`.
