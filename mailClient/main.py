"""
Chương trình chính khởi chạy ứng dụng Mail Client.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk  # Import thư viện chuẩn
from VIEW.mainView import MainView  # Import module nội bộ
from CONTROLLER.mainController import MainController
from loguru import logger

if __name__ == "__main__":
    logger.info("Khởi chạy ứng dụng Mail Client")
    root = tk.Tk()
    main_controller = MainController(MainView(root))
    root.mainloop()
