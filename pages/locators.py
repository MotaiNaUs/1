from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")

class LoginPageLocators:
    URL_CHECK = "login"
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    #LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_TEXT = (By.CSS_SELECTOR, ".alertinner")
    TOTAL_COAST = (By.XPATH,"//div[@class='alert alert-safe alert-noicon alert-info  fade in']/div/p[1]/strong")
    BOOK_COAST = (By.CSS_SELECTOR, "p.price_color")
