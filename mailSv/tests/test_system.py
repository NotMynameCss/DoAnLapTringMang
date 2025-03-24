import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_flow(self):
        driver = self.driver
        driver.get("http://localhost:8000")
        username_field = driver.find_element_by_name("username")
        password_field = driver.find_element_by_name("password")
        login_button = driver.find_element_by_name("login")

        username_field.send_keys("testuser")
        password_field.send_keys("testpass")
        login_button.click()

        self.assertIn("Dashboard", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
