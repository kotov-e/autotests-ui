import allure
from playwright.sync_api import Page, Locator, expect
from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


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

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает объект Locator для текущего элемента
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора (динамические значения)
        :return: объект-локатор
        """
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs) -> None:
        """
        Клик по элементу
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        # "ленивая" инициализация
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            # инициализация только во время вызова метода click
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        """
        Проверка видимости элемента
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        step = f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        """
        Проверка, что элемент содержит ожидаемый текст
        :param nth: индекс элемента по порядку
        :param text: ожидаемый текст
        :param kwargs: параметры для форматирования локатора
        """
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)
