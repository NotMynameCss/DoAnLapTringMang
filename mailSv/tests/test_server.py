import json
import unittest
from server import handle_delete_email
from CONTROLLER.mailController import MailController

class TestServer(unittest.TestCase):
    def setUp(self):
        self.mail_controller = MailController()

    def test_handle_delete_email_success(self):
        response = handle_delete_email(self.mail_controller, 1, "test_user")
        self.assertIn("success", response)
        self.assertTrue(json.loads(response)["success"])

    def test_handle_delete_email_invalid_id(self):
        response = handle_delete_email(self.mail_controller, -1, "test_user")
        self.assertIn("success", response)
        self.assertFalse(json.loads(response)["success"])
