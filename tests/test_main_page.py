import pytest

from tests.pages.locators import MainPageLocators, BasketPage
from tests.pages.product_page import ProductPage
from tests.pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_user_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.BUTTON_GO_TO_BASKET).click()
    page.is_not_element_present(*BasketPage.TEXT_YOUR_BASKET_IS_NOT_EMPTY)
    text = browser.find_element(*BasketPage.TEXT_YOUR_BASKET_IS_EMPTY).get_attribute('textContent')
    page.guest_see_text_your_basket_is_emty(text)


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
                                  "promo=offer5", "promo=offer6", "promo=offer7", "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{link}"
    page = MainPage(browser, link)
    page.open()
    page.click_on_button(*MainPageLocators.BUTTON_ADD_TO_BASKET)
    page.solve_quiz_and_get_code()
    page.should_be_basket_massegrs()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    link1 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page = MainPage(browser, link)
    page.open()
    page.click_on_button(*MainPageLocators.BUTTON_ADD_TO_BASKET)
    page.solve_quiz_and_get_code()
    page_basket = ProductPage(browser, link1)
    page_basket.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    link1 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page = MainPage(browser, link)
    page.open()
    page.click_on_button(*MainPageLocators.BUTTON_ADD_TO_BASKET)
    page.solve_quiz_and_get_code()
    page_basket = ProductPage(browser, link1)
    page_basket.should_dissapear_of_success_message()
