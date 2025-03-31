import unittest
from CONTROLLER.mailController import MailController

class TestMailController(unittest.TestCase):
    def setUp(self):
        self.controller = MailController("test_user")

    def test_send_email_success(self):
        email_data = {
            "sender": "test_user",
            "recipients": "recipient@example.com",
            "cc": "",
            "bcc": "",
            "subject": "Test Subject",
            "body": "Test Body",
            "attachments": ""
        }
        response = self.controller.send_email(email_data)
        self.assertIn("thành công", response.lower())

    def test_send_email_invalid_data(self):
        email_data = {
            "sender": "",
            "recipients": "",
            "cc": "",
            "bcc": "",
            "subject": "",
            "body": "",
            "attachments": ""
        }
        response = self.controller.send_email(email_data)
        self.assertIn("lỗi xác thực dữ liệu", response.lower())
