import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания задания
        self.exercises_title = Text(
            page=page,
            locator='create-course-exercises-box-toolbar-title-text',
            name='Title'
        )

        self.create_exercises_button = Button(
            page=page,
            locator='create-course-exercises-box-toolbar-create-exercise-button',
            name='Button'
        )

    @allure.step('Checking visible create course exercise toolbar and create exercises button')
    def check_visible(self):
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')
        self.create_exercises_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercises_button.click()