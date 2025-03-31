# Hướng dẫn sử dụng Controller trong thư mục `mailSv`

## Tổng quan
Thư mục `mailSv` chứa các thành phần Controller, tuân thủ mô hình MVC và nguyên tắc SOLID. Controllers xử lý logic nghiệp vụ, tương tác với cơ sở dữ liệu và quản lý kết nối mạng.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính
- **TCP/IP**: Giao thức mạng qua cổng 65432
- **SQLAlchemy 2.0.39**: ORM với connection pooling
- **Pydantic 2.10.6**: Validate dữ liệu
- **Loguru 0.7.3**: Logging chi tiết

## Cấu trúc Controller

### 1. Base Controller
- **Chức năng**: Lớp cơ sở cho các controller
- **Tính năng mới**:
  - Connection pooling
  - Retry mechanism
  - Error handling thống nhất

### 2. AuthController
- **Chức năng**: Xác thực người dùng
- **Phương thức chính**:
  ```python
  def login(username: str, password: str) -> dict
  def register(username: str, password: str) -> dict
  ```

### 3. MailController  
- **Chức năng**: Quản lý email
- **Phương thức chính**:
  ```python
  def send_email(data: EmailModel) -> dict
  def fetch_emails(type: str) -> list
  def delete_email(id: int) -> dict
  ```

## Cải tiến mới

### 1. Network
- Timeout management
- ACK mechanism
- Retry with backoff

### 2. Database
- Connection pooling
- Lazy loading
- Transaction management

### 3. Validation
- Pydantic models
- Error handlers
- Type checking

## Các nguyên tắc phát triển

### 1. Clean Code
- SOLID principles
- DRY/KISS
- Meaningful names

### 2. Error Handling
- Try-except blocks
- Error logging
- User feedback

### 3. Testing
- Unit tests
- Integration tests  
- Coverage reports

## Usage Examples

### Initialization
```python
from CONTROLLER.mailController import MailController

controller = MailController()
```

### Send Email
```python 
result = controller.send_email({
    "sender": "user@example.com",
    "recipients": ["to@example.com"],
    "subject": "Test",
    "body": "Hello"
})
```

### Delete Email
```python
result = controller.delete_email(
    email_id=123,
    user_id="user@example.com"
)
```

## Lưu ý quan trọng
- Sử dụng try-except cho các thao tác database/network
- Luôn validate input với Pydantic
- Ghi log mọi lỗi quan trọng
