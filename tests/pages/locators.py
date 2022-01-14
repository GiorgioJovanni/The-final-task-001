from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')


class LoginPageLocators:
    ID_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    ID_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")



