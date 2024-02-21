from fixtures.base import BaseTestCase
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class MainPage(BaseTestCase):
    def click_signup_button(self):
        self.wait.until(ec.element_to_be_clickable((By.ID("gift-dt-link")))).click()