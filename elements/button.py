from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    """
    Класс элемента button
    """

    def check_enabled(self, **kwargs) -> None:
        """
        Метод проверки, что кнопка доступна
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs) -> None:
        """
        Метод проверки, что кнопка не доступна
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()
