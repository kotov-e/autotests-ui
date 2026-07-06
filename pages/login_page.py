from components.authentivation.login_form_component import LoginFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)