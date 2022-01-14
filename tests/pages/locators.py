from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_GO_YO_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')


class LoginPageLocators:
    ID_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    ID_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPage:
    TEXT_YOUR_BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")



