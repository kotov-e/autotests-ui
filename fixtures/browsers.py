from symtable import Function

import pytest
import allure

from playwright.sync_api import Page, Playwright, expect

from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

from tools.playwright.pages import inittialize_playwright_page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    print("[FIXTURE] Create new user")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from inittialize_playwright_page(
        playwright,
        test_name=request.node.name
    )


@pytest.fixture()
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from inittialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state='browser-state.json'
    )
