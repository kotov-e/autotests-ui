from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class Input(BaseElement):
    """
    Класс элемента input
    """
    def get_locator(self, **kwargs) -> Locator:
        """
        Переопределение локатора, добавляем input
        :param kwargs: параметры для форматирования локатора
        """
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, **kwargs) -> None:
        """
        Метод заполнения поля

        :param value: значение поля
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs) -> None:
        """
        Проверка, что элемент содержит ожидаемый текст
        :param value: ожидаемое значение
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
