from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
import allure


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(
            page=page,
            locator='login-form-email-input',
            name='Email'
        )
        self.password_input = Input(
            page=page,
            locator='login-form-password-input',
            name='Password'
        )

    @allure.step('Fill login form')
    def fill(self, email: str, password: str) -> None:
        """
        Метод для заполнения формы логин

        :param email: email пользователя
        :param password: password пользователя
        """
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step('Check visible login form')
    def check_visible(self, email: str, password: str) -> None:
        """
        Проверка видимости элементов

        :param email: email
        :param password: password
        """
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
