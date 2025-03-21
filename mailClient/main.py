import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from VIEW.mainView import MainView
from CONTROLLER.mainController import MainController
from loguru import logger
from pydantic import ValidationError
from MODEL.models import RegisterModel, LoginModel  # Import models from models.py

if __name__ == "__main__":
    root = tk.Tk()
    main_controller = MainController(MainView(root))
    root.mainloop()
