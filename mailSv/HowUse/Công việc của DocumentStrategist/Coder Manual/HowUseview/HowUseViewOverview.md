# Tổng quan về cách view của toàn bộ code `mailSv` hoạt động

## Tổng quan
Dự án `mailSv` là một ứng dụng Mail Server được xây dựng bằng Python, sử dụng giao thức TCP/IP để kết nối giữa client và server. Ứng dụng này tuân theo mô hình MVC (Model-View-Controller) để tách biệt các thành phần giao diện, logic nghiệp vụ và dữ liệu.

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

## Mô hình MVC
- **Model**: Quản lý dữ liệu và logic nghiệp vụ của ứng dụng.
- **View**: Quản lý giao diện người dùng và hiển thị dữ liệu.
- **Controller**: Xử lý các yêu cầu từ người dùng, tương tác với Model và cập nhật View.

## Các thành phần chính của View

### 1. `mainView.py`
- **Chức năng**: Khởi tạo giao diện chính của ứng dụng, bao gồm việc hiển thị giao diện đăng nhập.
- **Thành phần**:
  - `AuthView`: Hiển thị giao diện đăng nhập và đăng ký.

### 2. `authView.py`
- **Chức năng**: Quản lý giao diện đăng nhập và đăng ký người dùng.
- **Thành phần**:
  - `EntryFrame`: Khung nhập liệu cho tài khoản và mật khẩu.
  - `ButtonFrame`: Khung chứa các nút chức năng (Đăng nhập, Đăng ký).

### 3. `mailView.py`
- **Chức năng**: Quản lý giao diện chính sau khi đăng nhập thành công.
- **Thành phần**:
  - `TopFrame`: Khung trên cùng chứa thanh tìm kiếm và nút soạn thư mới.
  - `LeftFrame`: Khung bên trái chứa các nút điều hướng (Hộp thư đến, Đã gửi, Thư nháp, Thùng rác, Nhãn, Cài đặt, Chat/Meet).
  - `RightFrame`: Khung bên phải hiển thị danh sách người dùng và chi tiết người dùng.

## Chi tiết các thành phần View

### `TopFrame`
- **Chức năng**: Chứa thanh tìm kiếm và nút soạn thư mới.
- **Thành phần**:
  - `compose_button`: Nút Soạn Thư.
  - `search_entry`: Ô tìm kiếm.
  - `search_button`: Nút Tìm Kiếm.
  - `refresh_button`: Nút Làm mới.

### `LeftFrame`
- **Chức năng**: Chứa các nút điều hướng.
- **Thành phần**:
  - `inbox_button`: Nút Hộp thư đến.
  - `sent_button`: Nút Đã gửi.
  - `drafts_button`: Nút Thư nháp.
  - `trash_button`: Nút Thùng rác.
  - `labels_button`: Nút Nhãn.
  - `settings_button`: Nút Cài đặt.
  - `chat_button`: Nút Chat/Meet.

### `RightFrame`
- **Chức năng**: Hiển thị danh sách người dùng và chi tiết người dùng.
- **Thành phần**:
  - `user_listbox`: Danh sách người dùng.
  - `user_details_tree`: Chi tiết người dùng.

## Nguyên tắc thiết kế
- **Tách biệt mối quan tâm (Separation of Concerns - SoC)**: Tách biệt rõ ràng giữa lớp trình diễn và lớp logic kinh doanh.
- **Nguyên tắc đơn nhiệm (Single Responsibility Principle - SRP)**: Mỗi lớp chỉ thực hiện một nhiệm vụ duy nhất.
- **Nguyên tắc đảo ngược phụ thuộc (Dependency Inversion Principle - DIP)**: Sử dụng các giao diện và các lớp trừu tượng để giảm thiểu sự phụ thuộc.
- **Mẫu thiết kế MVC (Model-View-Controller)**: Áp dụng mẫu thiết kế MVC để tách biệt rõ ràng giữa các lớp.

## Lưu ý
- Các thông báo và lỗi sẽ được hiển thị bằng tiếng Việt để dễ hiểu.
- Mọi thao tác và sự kiện đều được xử lý thông qua các controller tương ứng.

Hy vọng tài liệu này sẽ giúp bạn hiểu rõ hơn về cách hoạt động của các view trong thư mục `mailSv`.
