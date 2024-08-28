import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_key(browser):
    browser.get(link)
    assert browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"), "Кнопка добавления в корзину не найдена"
    time.sleep(5)