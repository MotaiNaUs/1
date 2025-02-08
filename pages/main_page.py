from project_1.pages.base_page import BasePage
from project_1.pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
      assert self.is_element_visible(*MainPageLocators.LOGIN_LINK), "every thing is bad"