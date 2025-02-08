from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_visible(self):
        self.is_element_visible(*ProductPageLocators.ADD_BUTTON)
    def add_product_to_card(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_success_message(self):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT).text
        print(message)
        assert "The shellcoder's handbook" in message, "not right book"

    def check_is_coast_right(self):
        total_coast = self.browser.find_element(*ProductPageLocators.TOTAL_COAST).text
        book_coast = self.browser.find_element(*ProductPageLocators.BOOK_COAST).text
        print(total_coast, "gkd")
        print(book_coast, "dkfjs")
        assert book_coast in total_coast, "not right price"