import unittest
from CONTROLLER.mailController import MailController
from unittest.mock import MagicMock

class TestMailController(unittest.TestCase):
    def setUp(self):
        self.mail_controller = MailController()
        self.mail_controller.fetch_mail_controller = MagicMock()
        self.mail_controller.send_mail_controller = MagicMock()
        self.mail_controller.search_mail_controller = MagicMock()

    def test_send_email(self):
        self.mail_controller.send_mail_controller.send_email.return_value = "Email đã được gửi thành công"
        result = self.mail_controller.send_email("sender", "recipients", "cc", "bcc", "subject", "body", "attachments")
        self.assertEqual(result, "Email đã được gửi thành công")

    def test_fetch_emails(self):
        self.mail_controller.fetch_mail_controller.fetch_emails.return_value = []
        result = self.mail_controller.fetch_emails("inbox")
        self.assertEqual(result, [])

    def test_search_emails(self):
        self.mail_controller.search_mail_controller.search_emails.return_value = []
        result = self.mail_controller.search_emails("query")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
