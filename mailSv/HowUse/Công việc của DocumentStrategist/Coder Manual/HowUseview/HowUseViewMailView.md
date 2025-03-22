# Hướng dẫn sử dụng giao diện `mailView` trong thư mục `mailSv`

## Tổng quan
Giao diện `mailView` trong thư mục `mailSv` được sử dụng để quản lý email sau khi người dùng đăng nhập thành công. Giao diện này được xây dựng bằng thư viện Tkinter của Python và tuân theo mô hình MVC (Model-View-Controller).

## Các thành phần chính

### 1. `mailView.py`
- Đây là giao diện chính của `mailView`.
- Người dùng có thể xem, tìm kiếm, và làm mới danh sách email.
- Giao diện bao gồm các khung chính: `top_frame`, `left_frame`, `right_frame`.

### 2. `topFrame.py`
- Khung trên cùng chứa thanh tìm kiếm và nút soạn thư mới.
- Bao gồm các thành phần:
  - **Nút Soạn Thư** (`compose_button`): Khi nhấn vào, sẽ gọi hàm `compose_email` để mở giao diện soạn email mới.
  - **Ô tìm kiếm** (`search_entry`): Người dùng có thể nhập từ khóa để tìm kiếm email.
  - **Nút Tìm Kiếm** (`search_button`): Khi nhấn vào, sẽ gọi hàm `search_email` để thực hiện tìm kiếm email.
  - **Nút Làm mới** (`refresh_button`): Khi nhấn vào, sẽ gọi hàm `refresh_emails` để làm mới danh sách email.

### 3. `leftFrame.py`
- Khung bên trái chứa các nút điều hướng như Hộp thư đến, Đã gửi, Thư nháp, Thùng rác, Nhãn.
- Bao gồm các thành phần:
  - **Nút Hộp thư đến** (`inbox_button`): Khi nhấn vào, sẽ gọi hàm `show_inbox` để hiển thị hộp thư đến.
  - **Nút Đã gửi** (`sent_button`): Khi nhấn vào, sẽ gọi hàm `show_sent` để hiển thị thư đã gửi.
  - **Nút Thư nháp** (`drafts_button`): Khi nhấn vào, sẽ gọi hàm `show_drafts` để hiển thị thư nháp.
  - **Nút Thùng rác** (`trash_button`): Khi nhấn vào, sẽ gọi hàm `show_trash` để hiển thị thùng rác.
  - **Nút Nhãn** (`labels_button`): Khi nhấn vào, sẽ gọi hàm `show_labels` để hiển thị nhãn.
  - **Nút Cài đặt** (`settings_button`): Khi nhấn vào, sẽ gọi hàm `show_settings` để hiển thị cài đặt.
  - **Nút Chat/Meet** (`chat_button`): Khi nhấn vào, sẽ gọi hàm `show_chat` để hiển thị chức năng Chat/Meet.

### 4. `rightFrame.py`
- Khung bên phải hiển thị danh sách người dùng và chi tiết người dùng.
- Bao gồm các thành phần:
  - **Danh sách người dùng** (`user_listbox`): Hiển thị danh sách tất cả người dùng từ cơ sở dữ liệu.
  - **Chi tiết người dùng** (`user_details_tree`): Hiển thị chi tiết thông tin người dùng khi được chọn từ danh sách.

## Chi tiết giao diện `mailView.py`

### Khởi tạo giao diện
- Khi khởi tạo, `MailView` sẽ thiết lập các khung và các thành phần giao diện.
- Gọi hàm `show_users` để hiển thị danh sách người dùng từ cơ sở dữ liệu.

### Soạn email mới
- Khi nhấn nút Soạn Thư, hàm `compose_email` sẽ được gọi và hiển thị thông báo rằng chức năng chưa được triển khai.

### Tìm kiếm email
- Khi nhấn nút Tìm Kiếm, hàm `search_email` sẽ được gọi để tìm kiếm email dựa trên từ khóa nhập vào ô tìm kiếm.

### Hiển thị hộp thư đến
- Khi nhấn nút Hộp thư đến, hàm `show_inbox` sẽ được gọi để hiển thị danh sách email trong hộp thư đến.

### Hiển thị thư đã gửi
- Khi nhấn nút Đã gửi, hàm `show_sent` sẽ được gọi để hiển thị danh sách email đã gửi.

### Làm mới danh sách email
- Khi nhấn nút Làm mới, hàm `refresh_emails` sẽ được gọi để làm mới danh sách email.

### Hiển thị danh sách người dùng
- Hàm `show_users` sẽ được gọi khi khởi tạo giao diện để hiển thị danh sách người dùng từ cơ sở dữ liệu.

### Hiển thị chi tiết người dùng
- Khi chọn một người dùng từ danh sách, hàm `on_user_select` sẽ được gọi để hiển thị chi tiết email của người dùng đó.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của giao diện `mailView` trong thư mục `mailSv`.
