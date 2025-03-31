# Hướng dẫn triển khai hệ thống mailServer

## Tổng quan
Hướng dẫn này cung cấp các bước chi tiết để triển khai hệ thống mailServer. Hệ thống được xây dựng bằng Python và sử dụng các công nghệ như XAMPP, Tkinter, và giao thức TCP/IP qua cổng `65432`.

## Cải tiến mới
- **Cổng mới**: Hệ thống sử dụng cổng `65432` để giao tiếp giữa client và server.
- **Connection Pooling**: Kích hoạt Connection Pooling trong SQLAlchemy để cải thiện hiệu suất.
- **Quản lý timeout**: Thêm cơ chế quản lý timeout cho kết nối TCP.

### 1. Chuẩn bị môi trường
...existing steps...

### 2. Cài đặt và cấu hình cơ sở dữ liệu
...existing steps...

### 3. Cấu hình Connection Pooling
- Mở file `dbconnector.py` và thêm cấu hình sau:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Kích hoạt Connection Pooling
engine = create_engine(
    "mysql+pymysql://username:password@localhost/mailserver",
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
)
Session = sessionmaker(bind=engine)
```

### 4. Quản lý timeout cho kết nối TCP
- Mở file `server.py` và thêm cấu hình timeout:
```python
from twisted.internet import reactor

# Cấu hình timeout
reactor.listenTCP(65432, factory, timeout=30)
```

### 5. Kiểm tra cấu hình mạng
- Đảm bảo rằng cổng `65432` được mở trên tường lửa.
- Sử dụng lệnh sau để kiểm tra trạng thái cổng:
```sh
netstat -an | find "65432"
```

...existing steps...
