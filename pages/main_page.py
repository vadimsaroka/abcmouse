from asyncio import sleep
from fixtures.base import BaseTestCase
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class MainPage(BaseTestCase):
    def click_signup_button(self):
        # TODO: chain shadow_root to get access to necessary element(Sign up button) 
        # moving from top to buttom  
        # <route-view/> -> <home-element/> -> <home-header/> -> <authstate-context/> -> <signup-button/>
        # like this: element1.shadow_root.getElementByCS(#).shadow_root (5 levels deep)
        self.wait.until(ec.element_to_be_clickable((By.XPATH('//*[@aria-label="Sign Up for ABCmouse.com"]')))).click()
