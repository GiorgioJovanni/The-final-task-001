from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    ID_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    ID_LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

