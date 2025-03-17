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
