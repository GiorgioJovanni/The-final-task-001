from tests.pages.base_page import BasePage


class BasketPage(BasePage):
    def user_is_in_basket(self):
        link = self.browser.current_url
        assert "http://selenium1py.pythonanywhere.com/en-gb/basket/" == link, "User is not in basket"
