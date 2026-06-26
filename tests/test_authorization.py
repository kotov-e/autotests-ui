import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        input_email = page.get_by_test_id('login-form-email-input').locator('input')
        input_email.fill('user.name@gmail.com')

        input_password = page.get_by_test_id('login-form-password-input').locator('input')
        input_password.fill('Password123')

        button_login = page.get_by_test_id('login-page-login-button')
        button_login.click()

        wrong_email_or_password_alert = page.get_by_test_id ('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

        page.wait_for_timeout(2000)


