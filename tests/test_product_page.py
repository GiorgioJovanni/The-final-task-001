from tests.pages.locators import BasePageLocators, LoginPageLocators, MainPageLocators, BasketPage
from tests.pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*BasePageLocators.LOGIN_LINK).click()
    page.is_element_present(*LoginPageLocators.ID_LOGIN_FORM)


def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.BUTTON_GO_TO_BASKET).click()
    text = browser.find_element(*BasketPage.TEXT_YOUR_BASKET_IS_EMPTY).get_attribute('textContent')
    page.guest_see_text_your_basket_is_emty(text)
