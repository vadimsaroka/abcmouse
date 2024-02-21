import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from fixtures.params import EXPLICIT_TIMEOUT, BROWSER_TYPE, HEADLESS


def get_browser():
    if BROWSER_TYPE.lower().find("chrome") >= 0:
        options = webdriver.ChromeOptions()
        if(HEADLESS):
            options.add_argument('--headless')
        options.page_load_strategy = 'eager'
        browser = webdriver.Chrome(options=options)
    elif BROWSER_TYPE.lower().find("firefox") >= 0:
        browser = webdriver.Firefox()
    else:
        raise Exception(f"I'm sorry {BROWSER_TYPE} browser is not supported")
    return browser

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = get_browser()
            cls.driver.maximize_window()
            cls.wait = WebDriverWait(cls.driver, timeout=EXPLICIT_TIMEOUT, poll_frequency=1)
            cls.page_url = None
        except Exception as e:
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def alert_handling(self, text):
        """
        Helper method to accept the presence alert
        :params text: text value
        """
        sleep(2)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.assertEqual(alert_text, text)
        alert.accept()
    
    def get_current_url(self):
        """
        Helper method that returns current URL
        """
        return self.driver.current_url

    def go_to_page(self):
        """
        Helper method that allows going to the page URL
        defined on the page from which this method was called
        """
        try:
            sleep(2)
            self.driver.get(self.page_url)
            self.wait.until(ec.url_to_be(self.page_url))
        except TimeoutException:
            raise

if __name__ == '__main__':
    unittest.main(verbosity=2)