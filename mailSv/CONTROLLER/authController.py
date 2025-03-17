import os
from MODEL.dbconnector import create_connection
from mysql.connector import Error

# class AuthController:
#     def __init__(self, view):
#         self.view = view
#         if self.view is not None:
#             self.view.set_controller(self)
#         self.connection = create_connection()
#         self.verify_table_exists()

#     def verify_table_exists(self):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute("SHOW TABLES LIKE 'users'")
#             result = cursor.fetchone()
#             if not result:
#                 print("Bảng 'users' không tồn tại trong database")
#                 cursor.execute("""
#                     CREATE TABLE users (
#                         id INT AUTO_INCREMENT PRIMARY KEY,
#                         username VARCHAR(255) NOT NULL UNIQUE,
#                         password VARCHAR(255) NOT NULL
#                     )
#                 """)
#                 self.connection.commit()
#                 print("Bảng 'users' đã được tạo thành công")
#         except Error as e:
#             print(f"Lỗi khi kiểm tra hoặc tạo bảng 'users': {e}")

#     def login(self, username, password):
#         if self.connection is None:
#             return "Lỗi kết nối đến database"
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
#             user = cursor.fetchone()
#             if user:
#                 print(f"Đăng nhập thành công cho người dùng: {username}")  # Debug print
#                 return "Đăng nhập thành công"
#             return "Tên người dùng hoặc mật khẩu không hợp lệ"
#         except Error as e:
#             return f"Lỗi khi đăng nhập: {e}"

#     def register(self, username, password):
#         if self.connection is None:
#             return "Lỗi kết nối đến database"
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#             user = cursor.fetchone()
            
            
#             if user:
#                 return "Tên người dùng đã tồn tại"
#             cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#             self.connection.commit()
            
            
#             # Verify insertion
#             cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#             user = cursor.fetchone()
#             if user:
#                 print(f"Đăng ký thành công cho người dùng: {username}")  # Debug print
#                 return "Đăng ký thành công"
#             else:
#                 return "Lỗi khi xác minh đăng ký"
#         except Error as e:
#             return {
#                 "status": "error",
#                 "message": f"Lỗi khi đăng ký: {e}"
#             }


class AuthController:
    def __init__(self, view):
        self.view = view
        if self.view is not None:
            self.view.set_controller(self)
        self.connection = create_connection()
        self.verify_table_exists()

    def verify_table_exists(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES LIKE 'users'")
            result = cursor.fetchone()
            if not result:
                print("Bảng 'users' không tồn tại trong database")
                cursor.execute("""
                    CREATE TABLE users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(255) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL
                    )
                """)
                self.connection.commit()
                print("Bảng 'users' đã được tạo thành công")
        except Error as e:
            print(f"Lỗi khi kiểm tra hoặc tạo bảng 'users': {e}")

    def login(self, username, password):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print(f"Đăng nhập thành công cho người dùng: {username}")  
                return "Đăng nhập thành công"
            return "Tên người dùng hoặc mật khẩu không hợp lệ"
        except Error as e:
            return f"Lỗi khi đăng nhập: {e}"

    def register(self, username, password):
        if self.connection is None:
            return "Lỗi kết nối đến database"
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            if user:
                return "Tên người dùng đã tồn tại"
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            # Verify insertion
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            if user:
                print(f"Đăng ký thành công cho người dùng: {username}")  
                return "Đăng ký thành công"
            else:
                return "Lỗi khi xác minh đăng ký"
        except Error as e:
            return {
                "status": "error",
                "message": f"Lỗi khi đăng ký: {e}"
            }