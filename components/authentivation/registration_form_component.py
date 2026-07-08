from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def fill(self, email: str, username: str, password: str):
        """
        Метод для заполнения формы регистрация
        :param email: email пользователя
        :param username: username пользователя
        :param password: password пользователя
        """

        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)

        expect(self.registration_button).to_be_visible()
        expect(self.registration_button).to_be_enabled()

    def click_registration_button(self):
        """
        Метод клика по кнопке REGISTRATION
        """
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_link(self):
        """
        Метод перехода по ссылке link
        """
        self.login_link.click()