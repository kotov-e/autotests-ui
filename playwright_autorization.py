from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    input_email = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    input_email.fill('user.name@gmail.com')

    input_password = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    input_password.fill('Password')

    button_login = page.locator('//button[@data-testid="login-page-login-button"]')
    button_login.click()

    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")


    page.wait_for_timeout(2000)
