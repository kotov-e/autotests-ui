from playwright.sync_api import sync_playwright, expect, Page


def test_empty_courses_list(chromium_page_with_state: Page):

        page = chromium_page_with_state

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
