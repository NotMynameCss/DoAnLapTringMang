from CONTROLLER.authController import AuthController

class MainController:
    def __init__(self, view):
        self.view = view
        if self.view is not None:
            self.view.set_controller(self)

    def handle_login(self, username, password):
        # Handle login logic
        auth_controller = AuthController(self.view)
        return auth_controller.login(username, password)

    def handle_register(self, username, password):
        # Handle registration logic
        auth_controller = AuthController(self.view)
        return auth_controller.register(username, password)