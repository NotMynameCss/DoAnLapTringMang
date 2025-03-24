import unittest
from CONTROLLER.authController import AuthController
from unittest.mock import MagicMock

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock()
        self.auth_controller = AuthController(self.view)

    def test_login_success(self):
        self.auth_controller.session = MagicMock()
        self.auth_controller.session.query().filter_by().first.return_value = True
        result = self.auth_controller.login("testuser", "testpass")
        self.assertEqual(result, "Đăng nhập thành công")

    def test_login_failure(self):
        self.auth_controller.session = MagicMock()
        self.auth_controller.session.query().filter_by().first.return_value = None
        result = self.auth_controller.login("testuser", "wrongpass")
        self.assertEqual(result, "Tên người dùng hoặc mật khẩu không hợp lệ")

    def test_register_success(self):
        self.auth_controller.session = MagicMock()
        self.auth_controller.session.query().filter_by().first.return_value = None
        self.auth_controller.session.add = MagicMock()
        self.auth_controller.session.commit = MagicMock()
        result = self.auth_controller.register("newuser", "newpass")
        self.assertEqual(result, "Đăng ký thành công")

    def test_register_failure(self):
        self.auth_controller.session = MagicMock()
        self.auth_controller.session.query().filter_by().first.return_value = True
        result = self.auth_controller.register("existinguser", "newpass")
        self.assertEqual(result, "Tên người dùng đã tồn tại")

if __name__ == "__main__":
    unittest.main()
