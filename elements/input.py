from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement
import allure


class Input(BaseElement):
    """
    Класс элемента input
    """
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Переопределение локатора, добавляем input
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs) -> None:
        """
        Метод заполнения поля
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
