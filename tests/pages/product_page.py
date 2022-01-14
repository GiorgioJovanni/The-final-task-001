from base_page import BasePage
from locators import BasketPage


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert not self.is_not_element_present(*BasketPage.SUCCESS_MESSAGE), "Element is presented"

    def should_dissapear_of_success_message(self):
        assert True


