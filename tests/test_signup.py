from fixtures.params import DOMAIN
from pages.main_page import MainPage
from pages.sing_up_page import SignUpPage
from pages.subscription_page import SubscriptionPage


class TestSignUp(SignUpPage, MainPage, SubscriptionPage):
    def setUp(self):
        self.page_url = DOMAIN
        self.driver.delete_all_cookies()
        self.go_to_page()

    def test_sing_up(self):
        self.click_signup_button()
        self.verify_prospect_register_url()
        self.enter_your_email()
        self.click_submit_button()
        self.verify_subscription_page_url()
        self.verify_creare_your_account_header()
        self.verify_subscription_form_presentself()