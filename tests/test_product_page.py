import pytest

from tests.pages.login_page import LoginPage
from tests.pages.locators import BasePageLocators, LoginPageLocators, MainPageLocators, BasketPage
from tests.pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.register_new_fake_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.click_on_button(*MainPageLocators.BUTTON_ADD_TO_BASKET)
        page.click_on_button(*MainPageLocators.BUTTON_GO_TO_BASKET)
        page.is_element_present(*BasketPage.TEXT_BASKET_IS_NOT_EMPTY)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button(*MainPageLocators.BUTTON_GO_TO_BASKET)
    page.is_not_element_present(*BasketPage.TEXT_YOUR_BASKET_IS_NOT_EMPTY)
    page.guest_see_empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button(*BasePageLocators.LOGIN_LINK)
    page.is_element_present(*LoginPageLocators.ID_LOGIN_FORM)


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button(*MainPageLocators.GO_TO_LOGIN_FORM)
    page.register_new_fake_user()
    page.open()
    page.should_be_authorized_user()
    page.click_on_button(*MainPageLocators.BUTTON_ADD_TO_BASKET)
    page.click_on_button(*MainPageLocators.BUTTON_GO_TO_BASKET)
    page.is_element_present(*BasketPage.TEXT_BASKET_IS_NOT_EMPTY)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button(*MainPageLocators.BUTTON_ADD_TO_BASKET)
    page.click_on_button(*MainPageLocators.BUTTON_GO_TO_BASKET)
    page.is_element_present(*BasketPage.TEXT_BASKET_IS_NOT_EMPTY)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
