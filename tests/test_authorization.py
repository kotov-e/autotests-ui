import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    input_email = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    input_email.fill('user.name@gmail.com')

    input_password = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    input_password.fill('Password123')

    button_login = chromium_page.get_by_test_id('login-page-login-button')
    button_login.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    chromium_page.wait_for_timeout(2000)
