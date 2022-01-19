from tests.pages.base_page import BasePage
from tests.pages.locators import BasketPage


class ProductPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasketPage.SUCCESS_MESSAGE)
        login_link.click()

    def should_not_be_success_message(self):
        try:
            assert self.is_not_element_present(*BasketPage.SUCCESS_MESSAGE), "Element is presented"
        except AssertionError:
            print("Test failed")

    def should_dissapear_of_success_message(self):
        try:
            assert self.is_disappeared(*BasketPage.SUCCESS_MESSAGE), "Element is not disappeared"
        except AssertionError:
            print("Test failed")

    def guest_see_text_your_basket_is_emty(self, text):
        assert '\n            Your basket is empty.\n            Continue shopping\n        ' == text
