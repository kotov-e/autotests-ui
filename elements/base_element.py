from playwright.sync_api import Page, Locator, expect


class BaseElement:
    """
    Базовый класс, описывающий общую логику работы с элементами и их локаторами

    :param page: объект страницы, для взаимодействия со страницей и поиска элементов
    :param locator: строка-локатор элемента, чтобы указать, как мы будем находить элемент на странице
    :param name: имя элемента для формирования логов и отчетов
    """

    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, **kwargs) -> Locator:
        """
        Возвращает объект Locator для текущего элемента
        :param kwargs: параметры для форматирования локатора (динамические значения)
        :return: объект-локатор
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs) -> None:
        """
        Клик по элементу
        :param kwargs: параметры для форматирования локатора
        """
        # "ленивая" инициализация
        locator = self.get_locator(**kwargs)
        # инициализация только во время вызова метода click
        locator.click()

    def check_visible(self, **kwargs) -> None:
        """
        Проверка видимости элемента
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs) -> None:
        """
        Проверка, что элемент содержит ожидаемый текст
        :param text: ожидаемый текст
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
