import math

from tests.pages.base_page import BasePage
from tests.pages.locators import MainPageLocators, BasketPage, BasePageLocators
from tests.pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPage.SUCCESS_MESSAGE), "Element is presented"

    def should_be_basket_massegrs(self):
        assert self.is_element_present(*BasketPage.SUCCESS_MESSAGE), "Element is not presented"

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
