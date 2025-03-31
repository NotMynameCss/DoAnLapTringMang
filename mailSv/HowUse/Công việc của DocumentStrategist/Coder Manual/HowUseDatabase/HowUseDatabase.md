# Hướng dẫn sử dụng Database trong thư mục `mailSv`

## Tổng quan
Hệ thống sử dụng SQLAlchemy làm ORM chính để tương tác với MySQL database, kết hợp với Pydantic để validate dữ liệu và Connection Pooling để tối ưu hiệu suất.

## Công nghệ sử dụng
- **Python 3.13.2**: Ngôn ngữ lập trình chính.
- **Windows 10 64-bit**: Hệ điều hành phát triển và chạy ứng dụng.
- **XAMPP (xampp-windows-x64-8.2.12-0)**: Quản lý cơ sở dữ liệu.
- **SqlAlchemy 2.0.39**: ORM framework.
- **MySQL**: Database server.
- **Pydantic 2.10.6**: Data validation.
- **Connection Pooling**: Quản lý connection pool.

## Cấu trúc Database

### 1. Models
```python
class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    sender = Column(String(255))
    recipients = Column(Text)
    # ...existing fields...

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    # ...existing fields...
```

## Cấu hình Connection Pool
```python
engine = create_engine(
    'mysql+mysqlconnector://root:@localhost/mail_server_db',
    pool_size=10,  # Số lượng connection tối đa trong pool
    max_overflow=20,  # Số lượng connection có thể tạo thêm
    pool_timeout=30,  # Thời gian chờ connection
    pool_pre_ping=True  # Kiểm tra connection trước khi sử dụng
)
```

## Sử dụng Context Manager
```python
with DBConnection() as session:
    try:
        # Thực hiện các thao tác database
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Database error: {e}")
```

## Validation với Pydantic
```python
class EmailModel(BaseModel):
    sender: str
    recipients: str
    subject: str = ""
    body: str = ""
```

## Best Practices

### 1. Connection Management
- Sử dụng context manager để đảm bảo đóng connection.
- Kích hoạt connection pooling.
- Thiết lập timeout hợp lý.

### 2. Transaction Management
- Sử dụng try-except block.
- Rollback khi có lỗi.
- Commit sau khi hoàn thành.

### 3. Performance Optimization
- Sử dụng Lazy Loading cho relationships.
- Tạo indexes cho các trường thường query.
- Tối ưu các câu query.

## Xử lý lỗi Database

### 1. Connection Errors
```python
try:
    session = create_connection()
except OperationalError as e:
    logger.error(f"Cannot connect to database: {e}")
    # Thử kết nối lại sau 5 giây
    time.sleep(5)
    session = create_connection()
```

### 2. Transaction Errors
```python
try:
    with DBConnection() as session:
        # Database operations
        session.commit()
except IntegrityError as e:
    logger.error(f"Integrity error: {e}")
except SQLAlchemyError as e:
    logger.error(f"Database error: {e}")
```

## Monitoring và Debug

### 1. Logging
```python
# Cấu hình logging
logger.add("database.log", 
    rotation="1 MB",
    retention="10 days",
    level="DEBUG")

# Log database operations
logger.debug("Executing query: {}", query)
logger.info("Database connection established")
logger.error("Database error: {}", error)
```

### 2. Performance Metrics
- Theo dõi thời gian thực thi query.
- Giám sát connection pool.
- Kiểm tra memory usage.

## Lưu ý quan trọng
1. Luôn đóng session sau khi sử dụng.
2. Sử dụng try-except để xử lý lỗi.
3. Validate dữ liệu trước khi lưu.
4. Tối ưu các câu query phức tạp.

## Kế hoạch phát triển
1. Thêm database migration tool.
2. Tối ưu hóa query performance.
3. Cải thiện logging và monitoring.
4. Thêm cache layer.
