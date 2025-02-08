from project_1.pages.product_page import ProductPage
def test_guest_can_add_product_to_basket (browser):
    LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, LINK)
# open page
    product_page.open()
# check is page correct displayed
    product_page.should_be_visible()
# push add button
    product_page.add_product_to_card()
# start script
    product_page.solve_quiz_and_get_code()
# check success window and name is right
    product_page.check_success_message()
#check the price is actual
    product_page.check_is_coast_right()