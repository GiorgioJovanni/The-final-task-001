from tests.pages.base_page import BasePage
from tests.pages.locators import BasketPage, BasePageLocators
from tests.pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasePage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPage.SUCCESS_MESSAGE), "Element is presented"

    def should_be_basket_massages(self):
        assert self.is_element_present(*BasketPage.SUCCESS_MESSAGE), "Element is not presented"
