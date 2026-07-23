from elements.base_element import BaseElement
import allure
from tools.logger import get_logger

logger = get_logger("FILE_INPUT_ELEMENT")


class FileInput(BaseElement):
    """
    Класс элемента file input (загрузка файла)
    """

    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str, nth: int = 0, **kwargs) -> None:
        """
        Метод загрузки файла
        :param file: путь к файлу
        :param nth: индекс элемента по порядку
        :param kwargs: параметры для форматирования локатора
        """
        step = f'Set file "{file}" to the {self.type_of} "{self.name}'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)
