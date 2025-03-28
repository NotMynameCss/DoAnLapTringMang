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
from twisted.internet import reactor
from utils.logger import get_twisted_logger

twisted_logger = get_twisted_logger()

def start_tkinter_app():
    root = tk.Tk()
    main_view = MainView(root)
    main_controller = MainController(main_view)
    main_view.set_controller(main_controller)
    root.mainloop()

if __name__ == "__main__":
    # Initialize controllers
    mail_controller = MailController()
    main_view = MainView(tk.Tk())
    main_controller = MainController(main_view)
    main_view.set_controller(main_controller)

    # Start the Twisted server in a separate thread
    threading.Thread(target=start_server, args=(main_controller, mail_controller)).start()

    # Start the Tkinter application in the main thread
    start_tkinter_app()

    # Start the Twisted reactor in the main thread
    reactor.run()
