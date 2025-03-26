import unittest
from CONTROLLER.emailController import EmailController

class TestEmailController(unittest.TestCase):
    def setUp(self):
        self.controller = EmailController()

    def test_delete_email_invalid_id(self):
        result = self.controller.delete_email(-1, "test_user")
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Email ID không hợp lệ")

    def test_delete_email_invalid_user(self):
        result = self.controller.delete_email(1, "")
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "User ID không hợp lệ")

    def test_delete_email_nonexistent(self):
        result = self.controller.delete_email(99999, "test_user")
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Email không tồn tại hoặc bạn không có quyền xóa")
