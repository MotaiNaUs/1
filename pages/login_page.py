from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert LoginPageLocators.URL_CHECK in url, "not right url"

    def should_be_login_form(self):
        assert self.is_element_visible(*LoginPageLocators.LOG_FORM), "no login form"
    def should_be_register_form(self):
        assert self.is_element_visible(*LoginPageLocators.REG_FORM), "no register form"
