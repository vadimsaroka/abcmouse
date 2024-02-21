from fixtures.base import BaseTestCase
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class SubscriptionPage(BaseTestCase):
    def verify_subscription_page_url(self):
        expected_url = "https://www.abcmouse.com/abc/subscription/"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Actual URL '{actual_url}' does not match expected URL '{expected_url}'"
    
    def verify_creare_your_account_header(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH("//h3[contains(text(),'Create Your Account')]"))))

    def verify_subscription_form_presentself(self):
        self.wait.until(ec.presence_of_element_located((By.ID("subscription-form"))))