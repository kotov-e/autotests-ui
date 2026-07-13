import pytest
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
import allure

from tools.allure.tags import AllureTag
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercise_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Courses Playwright + Pytest",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.navbar.check_visible(username='username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self,
                         create_course_page: CreateCoursePage,
                         courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Courses Playwright + Pytest",
            max_score="100",
            min_score="10")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.menu.click_edit()
        create_course_page.create_course_form.fill(
            title="Playwright_1",
            estimated_time="3 weeks",
            description="Courses Playwright + Pytest + Allure + coverage",
            max_score="90",
            min_score="20")
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright_1",
            estimated_time="3 weeks",
            max_score="90",
            min_score="20"
        )
