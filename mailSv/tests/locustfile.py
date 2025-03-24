from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def login(self):
        self.client.post("/login", {"username": "testuser", "password": "testpass"})

    @task(2)
    def send_email(self):
        self.client.post("/send_email", {
            "sender": "testuser",
            "recipients": "recipient@example.com",
            "cc": "",
            "bcc": "",
            "subject": "Test Email",
            "body": "This is a test email.",
            "attachments": ""
        })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
