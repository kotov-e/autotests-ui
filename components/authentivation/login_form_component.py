from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def fill(self, email: str, password: str):
        """
        Метод для заполнения формы логин
        :param email: email пользователя
        :param password: password пользователя
        """
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)

        expect(self.login_button).to_be_visible()
        expect(self.login_button).to_be_enabled()

        expect(self.registration_link).to_be_visible()
        expect(self.registration_link).to_be_enabled()

    def click_login_button(self):
        """
        Метод клика по кнопке LOGIN
        """
        self.login_button.click()

    def click_registration_link(self):
        """
        Метод перехода по ссылке registration
        """
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        """
        Проверка наличие алерта Wrong email or password
        """
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text('Wrong email or password')
