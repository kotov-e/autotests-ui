from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Класс элемента file input (загрузка файла)
    """

    def set_input_files(self, file: str, **kwargs) -> None:
        """
        Метод загрузки файла
        :param file: путь к файлу
        :param kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)
