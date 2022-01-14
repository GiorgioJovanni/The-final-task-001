import time

import pytest

from locators import MainPageLocators
from tests.pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
                                  "promo=offer5", "promo=offer6", "promo=offer7", "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{link}"
    page = MainPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.BUTTON_ADD_TO_BASKET).click()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_basket_massegrs()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = MainPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.BUTTON_ADD_TO_BASKET).click()
    page.solve_quiz_and_get_code()
