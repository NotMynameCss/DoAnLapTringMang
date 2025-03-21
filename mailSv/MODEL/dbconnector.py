import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Thay đổi nếu bạn có user khác
            password='',  # Thay đổi nếu bạn có mật khẩu
            database='mail_server_db'  # Tên database của bạn
        )
        if connection.is_connected():
            print("Kết nối thành công đến database")
        return connection
    except Error as e:
        print(f"Lỗi kết nối đến database: {e}")
        return None

def create_email_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emails (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sender VARCHAR(255) NOT NULL,
                recipients TEXT NOT NULL,
                cc TEXT,
                bcc TEXT,
                subject VARCHAR(255),
                body TEXT,
                attachments TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        print("Bảng 'emails' đã được tạo thành công")
    except Error as e:
        print(f"Lỗi khi tạo bảng 'emails': {e}")
