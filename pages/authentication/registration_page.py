import re

from components.authentiсation.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(
            page=page,
            locator='registration-page-registration-button',
            name='Registration'
        )

        self.login_link = Link(
            page=page,
            locator='registration-page-login-link',
            name='Link'
        )

    def click_registration_button(self):
        """
        Метод клика по кнопке REGISTRATION
        """
        self.registration_button.click()

    def click_login_link(self):
        """
        Метод перехода по ссылке link
        """
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))


