from fixtures.base import BaseTestCase
from fixtures.params import DEFAULT_EMAIL
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class SignUpPage(BaseTestCase):
    def enter_your_email(self, email=DEFAULT_EMAIL):
        self.wait.until(ec.element_to_be_clickable((By.ID("email")))).send_keys(email)

    def click_submit_button(self):
        self.wait.until(ec.element_to_be_clickable((By.ID("submit-button")))).click()

    def verify_prospect_register_url(self):
        expected_url = "https://www.abcmouse.com/abc/prospect-register/"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Actual URL '{actual_url}' does not match expected URL '{expected_url}'"


