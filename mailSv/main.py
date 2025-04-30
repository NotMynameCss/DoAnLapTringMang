# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from VIEW.mainView import MainView
from CONTROLLER.mainController import MainController
from CONTROLLER.mailController import MailController
from server import start_server
import threading
import socket
from network_config import SERVER_PORT

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if __name__ == "__main__":
    root = tk.Tk()
    main_controller = MainController(MainView(root))
    mail_controller = MailController()

    port = SERVER_PORT  # Sử dụng PORT từ network_config
    if is_port_in_use(port):
        print(f"Port {port} is already in use. Please stop the other server or use a different port.")
    else:
        server_thread = threading.Thread(target=start_server, args=(main_controller, mail_controller))
        server_thread.start()

    root.mainloop()
