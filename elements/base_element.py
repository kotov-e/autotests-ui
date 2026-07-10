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
        self.locator = locator
        self.name = name

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает объект Locator для текущего элемента
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора (динамические значения)
        :return: объект-локатор
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs) -> None:
        """
        Клик по элементу
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        # "ленивая" инициализация
        locator = self.get_locator(nth, **kwargs)
        # инициализация только во время вызова метода click
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        """
        Проверка видимости элемента
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        """
        Проверка, что элемент содержит ожидаемый текст
        :param nth: индекс элемента по порядку
        :param text: ожидаемый текст
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
