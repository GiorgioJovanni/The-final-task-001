import pytest
import faker

from selenium import webdriver

from tests.pages.product_page import ProductPage
from tests.pages.login_page import LoginPage
from tests.pages.locators import MainPageLocators
from tests.pages.main_page import MainPage
from tests.pages.locators import LoginPageLocators


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# class TestUserAddToBasketFromProductPage:
#     # @pytest.fixture
#     # def setup(self):
#     #     link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
#     #     browser = webdriver.Chrome()  # открыть страницу регистрации;
#     #     f = faker.Faker()
#     #     email = f.email()
#     #     password = f.password()
#     #     LoginPage.register_new_user(email, password)  # зарегистрировать нового пользователя;
#     #     success_mesasge = browser.find_element(LoginPageLocators.SUCCESSFUL_MESSAGE_REGISTER)  # проверить, что пользователь залогинен.
#     #     el1 = success_mesasge.get_attribute('textContent')
#     #     assert "Спасибо за регистрацию!" == el1, "Registretion is not success"
#     #     return browser
#
#     def test_user_cant_see_success_message(self, browser):
#         link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
#         page = MainPage(browser, link)
#         page.open()
#         page.should_not_be_success_message()
#
#     def test_user_can_add_product_to_basket(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#         page = MainPage(browser, link)
#         page.open()
#         browser.find_element(*MainPageLocators.BUTTON_ADD_TO_BASKET).click()
#         page.should_be_basket_massegrs()
#
#     # def test_user_login_success(self):
#     #     linck = ''
