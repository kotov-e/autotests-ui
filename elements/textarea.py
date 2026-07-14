import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class TextArea(BaseElement):
    """
    Класс элемента textarea
    """

    @property
    def type_of(self) -> str:
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Переопределение локатора, добавляем textarea.first
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs) -> None:
        """
        Метод заполнения textarea
        :param value: значение поля
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs) -> None:
        """
        Проверка, что элемент содержит ожидаемый текст
        :param value: ожидаемое значение
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
