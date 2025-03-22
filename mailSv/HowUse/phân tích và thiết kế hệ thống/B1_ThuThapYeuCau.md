# Bước 1: Thu thập và phân tích yêu cầu của mailServer

## Tổng quan
Quá trình thu thập và phân tích yêu cầu là bước đầu tiên trong quy trình phát triển hệ thống. Mục tiêu của bước này là xác định các yêu cầu chức năng và phi chức năng của hệ thống mailServer dựa trên tiêu chuẩn.

## Yêu cầu chức năng
1. **Đăng nhập/Đăng ký**:
   - Người dùng có thể đăng ký tài khoản mới.
   - Người dùng có thể đăng nhập vào hệ thống bằng tài khoản đã đăng ký.

2. **Quản lý email**:
   - Người dùng có thể gửi email.
   - Người dùng có thể nhận email.
   - Người dùng có thể tìm kiếm email.
   - Người dùng có thể xóa email.
   - Người dùng có thể lưu email vào thư nháp.

3. **Quản lý người dùng**:
   - Người dùng có thể xem danh sách người dùng.
   - Người dùng có thể tìm kiếm người dùng.

4. **Quản lý nhãn**:
   - Người dùng có thể tạo nhãn mới.
   - Người dùng có thể gán nhãn cho email.
   - Người dùng có thể tìm kiếm email theo nhãn.

5. **Quản lý cài đặt**:
   - Người dùng có thể thay đổi cài đặt tài khoản.
   - Người dùng có thể thay đổi mật khẩu.

## Yêu cầu phi chức năng
1. **Hiệu suất**:
   - Hệ thống phải xử lý yêu cầu đăng nhập trong vòng 2 giây.
   - Hệ thống phải xử lý yêu cầu gửi email trong vòng 5 giây.

2. **Bảo mật**:
   - Hệ thống phải mã hóa mật khẩu người dùng.
   - Hệ thống phải bảo vệ dữ liệu người dùng khỏi các cuộc tấn công SQL Injection.

3. **Khả năng mở rộng**:
   - Hệ thống phải có khả năng mở rộng để hỗ trợ số lượng lớn người dùng.

4. **Khả năng bảo trì**:
   - Hệ thống phải dễ dàng bảo trì và nâng cấp.

5. **Khả năng sử dụng**:
   - Giao diện người dùng phải thân thiện và dễ sử dụng.

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

## Kết luận
Việc thu thập và phân tích yêu cầu là bước quan trọng để đảm bảo rằng hệ thống mailServer đáp ứng được các yêu cầu của người dùng và hoạt động hiệu quả. Các yêu cầu chức năng và phi chức năng đã được xác định rõ ràng sẽ là cơ sở để thiết kế và triển khai hệ thống.
