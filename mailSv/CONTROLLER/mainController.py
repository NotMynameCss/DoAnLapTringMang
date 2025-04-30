from CONTROLLER.authController import AuthController

class MainController:
    """Controller chính quản lý đăng nhập/đăng ký."""

    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)

    def handle_login(self, username, password):
        """Xử lý logic đăng nhập."""
        auth_controller = AuthController(self.view)
        return auth_controller.login(username, password)

    def handle_register(self, username, password):
        """Xử lý logic đăng ký."""
        auth_controller = AuthController(self.view)
        return auth_controller.register(username, password)