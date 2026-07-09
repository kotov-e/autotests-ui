from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class TextArea(BaseElement):
    """
    Класс элемента textarea
    """

    def get_locator(self, **kwargs) -> Locator:
        """
        Переопределение локатора, добавляем textarea.first

        :param kwargs: параметры для форматирования локатора
        """
        return super().get_locator(**kwargs).locator('textarea').first

    def fill(self, value: str, **kwargs) -> None:
        """
        Метод заполнения textarea

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
