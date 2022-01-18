from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    BUTTON_GO_TO_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')


class LoginPageLocators:
    ID_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    ID_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FIELD_FOR_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    FIELD_FOR_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    FIELD_FOR_PASSWORD_TWO = (By.CSS_SELECTOR, '[name="registration-password2"')
    BUTTON_REGISTER = (By.CSS_SELECTOR, '[name="registration_submit"]')
    SUCCESSFUL_MESSAGE_REGISTER = (By.CSS_SELECTOR, '.alertinner.wicon')


class BasketPage:
    TEXT_YOUR_BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")



