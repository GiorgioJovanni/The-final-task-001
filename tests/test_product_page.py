from locators import MainPageLocators, BasketPage
from main_page import MainPage
from product_page import ProductPage


def test_user_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    link1 = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    page = MainPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.BUTTON_GO_YO_BASKET).click()
    # time.sleep(99999)
    page_basket = ProductPage(browser, link1)
    text = browser.find_element(*BasketPage.TEXT_YOUR_BASKET_IS_EMPTY).get_attribute('textContent')
    page_basket.guest_see_text_your_basket_is_emty(text)


def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    link1 = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    page = MainPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.BUTTON_GO_YO_BASKET).click()
    # time.sleep(99999)
    page_basket = ProductPage(browser, link1)
    text = browser.find_element(*BasketPage.TEXT_YOUR_BASKET_IS_EMPTY).get_attribute('textContent')
    page_basket.guest_see_text_your_basket_is_emty(text)