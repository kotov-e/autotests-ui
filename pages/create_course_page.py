from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empy_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Верхний блок
        self.navbar = NavbarComponent(page)

        # Блок создания курса и кнопка создания курса
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)

        # Форма создания курса
        self.create_course_form = CreateCourseFormComponent(page)

        # Блок превью и загрузки картинки курса
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')

        # Блок заголовка и кнопка создания задания
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)

        # Блок, который отображается, когда в курсе нет заданий
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')

        # Блок создания занятий
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

    def check_visible_exercise_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
