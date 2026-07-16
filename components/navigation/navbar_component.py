import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.text import Text


class NavbarComponent(BaseComponent):
    """
    Верхний блок
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(
            page=page,
            locator='navigation-navbar-app-title-text',
            name='App title'
        )

        self.welcome_title = Text(
            page=page,
            locator='navigation-navbar-welcome-title-text',
            name='Welcome title'
        )

    @allure.step('Checking visible navbar')
    def check_visible(self, username: str) -> None:
        """
        Проверка видимости
        :param username:
        """
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')