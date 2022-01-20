from tests.pages.base_page import BasePage
from tests.pages.locators import BasketPage


class ProductPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasketPage.SUCCESS_MESSAGE)
        login_link.click()

    def guest_see_empty_basket(self):
        self.guest_see_text_your_basket_is_emty()
        self.guest_can_not_see_items_list()

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

    def guest_see_text_your_basket_is_emty(self):
        text = self.browser.find_element(*BasketPage.TEXT_YOUR_BASKET_IS_EMPTY).get_attribute('textContent')
        assert '\n            Your basket is empty.\n            Continue shopping\n        ' == text

    def guest_can_not_see_items_list(self):
        self.is_not_element_present(*BasketPage.ITEMS_LIST), "Basket is not empty"
