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

def start_tkinter_app():
    root = tk.Tk()
    main_view = MainView(root)
    main_controller = MainController(main_view)
    mail_controller = MailController()

    root.mainloop()

if __name__ == "__main__":
    # Start the Twisted server in the main thread
    root = tk.Tk()
    main_view = MainView(root)
    main_controller = MainController(main_view)
    mail_controller = MailController()
    threading.Thread(target=start_server, args=(main_controller, mail_controller)).start()

    # Start the Tkinter application in the main thread
    start_tkinter_app()

    # Start the Twisted reactor in the main thread
    reactor.run()
