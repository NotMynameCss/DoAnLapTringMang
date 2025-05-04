import unittest
from mailClient.CONTROLLER.mailController import MailController

class TestMailPermission(unittest.TestCase):
    def setUp(self):
        # Giả lập user "mod@gmail.com"
        self.mail_controller = MailController("mod@gmail.com")

    def test_no_access_to_other_users_mail(self):
        # Lấy tất cả email liên quan user hiện tại
        emails = self.mail_controller.fetch_all_emails()
        # Kiểm tra không có email nào mà sender/recipients/cc/bcc không chứa "mod@gmail.com"
        for email in emails:
            self.assertTrue(
                "mod@gmail.com" in email.get("sender", "") or
                "mod@gmail.com" in email.get("recipients", "") or
                "mod@gmail.com" in email.get("cc", "") or
                "mod@gmail.com" in email.get("bcc", ""),
                f"Email không thuộc về user: {email}"
            )

if __name__ == "__main__":
    unittest.main()
