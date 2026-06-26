from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        button_registration = page.get_by_test_id('registration-page-registration-button')
        expect(button_registration).to_be_disabled()

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        expect(button_registration).not_to_be_disabled()
        button_registration.click()

        dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        context = browser.new_context(storage_state='browser-state.json')

        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()

        icon_courses = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_courses).to_be_visible()

        courses_list_text_empty = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list_text_empty).to_be_visible()
        expect(courses_list_text_empty).to_have_text('There is no results')

        courses_list_empty_view_description_text = page.get_by_test_id(
            'courses-list-empty-view-description-text')
        expect(courses_list_empty_view_description_text).to_be_visible()
        expect(courses_list_empty_view_description_text).to_have_text(
            'Results from the load test pipeline will be displayed here')

        page.wait_for_timeout(2000)
