from .base_page import BasePage


from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        correct_url = self.browser.current_url
        assert correct_url == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/', \
            "Login url is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.ID_LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.ID_REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.fiend_element(*LoginPageLocators.FIELD_FOR_EMAIL).send_kyes(email)
        self.browser.fiend_element(*LoginPageLocators.FIELD_FOR_PASSWORD).send_kyes(password)
        self.browser.fiend_element(*LoginPageLocators.FIELD_FOR_PASSWORD_TWO).send_kyes(password)
        self.browser.fiend_element(*LoginPageLocators.BUTTON_REGISTER).click()


