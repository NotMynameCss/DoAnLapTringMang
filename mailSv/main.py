# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import socket
import threading
import tkinter as tk
from VIEW.mainView import MainView
from CONTROLLER.mainController import MainController


# # Cấu hình máy chủ
# HOST = 'localhost'
# PORT = 65432

# # Hàm xử lý kết nối từ client
# def handle_client(client_socket, main_controller):
#     try:
#         while True:
#             # Nhận tin nhắn từ client
#             message = client_socket.recv(1024).decode('utf-8')
#             if not message:
#                 break
#             print(f"Nhận tin nhắn: {message}")
            
#             # Xử lý các lệnh từ client
#             if message.startswith("REGISTER"):
#                 _, username, password = message.split()
#                 response = main_controller.register(username, password)
#             elif message.startswith("LOGIN"):
#                 _, username, password = message.split()
#                 response = main_controller.login(username, password)
#             else:
#                 response = "Lệnh không xác định"
            
#             # Gửi phản hồi lại cho client
#             client_socket.send(response.encode('utf-8'))
#             print(f"Phản hồi gửi đến client: {response}")  # Debug print
#     except Exception as e:
#         print(f"Lỗi: {e}")
#     finally:
#         client_socket.close()

# # Hàm chính để khởi động máy chủ
# def start_server(main_controller):
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((HOST, PORT))
#     server.listen(5)
#     print(f"Máy chủ đang lắng nghe trên {HOST}:{PORT}")

#     try:
#         while True:
#             client_socket, addr = server.accept()
#             print(f"Chấp nhận kết nối từ {addr}")
#             # Tạo một luồng mới để xử lý kết nối từ client
#             client_handler = threading.Thread(target=handle_client, args=(client_socket, main_controller))
#             client_handler.start()
#     except KeyboardInterrupt:
#         print("Máy chủ đang tắt")
#     finally:
#         server.close()

# if __name__ == "__main__":
#     main_controller = MainController(MainView(None))
#     # Khởi động máy chủ trong một luồng riêng
#     server_thread = threading.Thread(target=start_server, args=(main_controller,))
#     server_thread.start()

#     # Khởi động giao diện người dùng
#     root = tk.Tk()
#     app = MainView(root)
#     root.mainloop()

# Cấu hình máy chủ
HOST = 'localhost'
PORT = 65432

# Hàm xử lý kết nối từ client
def handle_client(client_socket, main_controller):
    try:
        while True:
            # Nhận tin nhắn từ client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Nhận tin nhắn: {message}")

            # Xử lý các lệnh từ client
            if message.startswith("REGISTER"):
                _, username, password = message.split()
                response = main_controller.handle_register(username, password)
            elif message.startswith("LOGIN"):
                _, username, password = message.split()
                response = main_controller.handle_login(username, password)
            else:
                response = "Lệnh không xác định"

            # Gửi phản hồi lại cho client
            client_socket.send(response.encode('utf-8'))
            print(f"Phản hồi gửi đến client: {response}")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        client_socket.close()

# Hàm chính để khởi động máy chủ
def start_server(main_controller):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Máy chủ đang lắng nghe trên {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Chấp nhận kết nối từ {addr}")
            # Tạo một luồng mới để xử lý kết nối từ client
            client_handler = threading.Thread(target=handle_client, args=(client_socket, main_controller))
            client_handler.start()
    except KeyboardInterrupt:
        print("Máy chủ đang tắt")
    finally:
        server.close()

if __name__ == "__main__":
    root = tk.Tk()
    main_controller = MainController(MainView(root))
    # Khởi động máy chủ trong một luồng riêng
    server_thread = threading.Thread(target=start_server, args=(main_controller,))
    server_thread.start()

    # Khởi động giao diện người dùng
    root.mainloop()
