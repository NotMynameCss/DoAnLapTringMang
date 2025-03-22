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

if __name__ == "__main__":
    root = tk.Tk()
    main_controller = MainController(MainView(root))
    mail_controller = MailController()

    server_thread = threading.Thread(target=start_server, args=(main_controller, mail_controller))
    server_thread.start()

    root.mainloop()
