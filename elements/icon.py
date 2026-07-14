from elements.base_element import BaseElement


class Icon(BaseElement):
    """
    Класс элемента icon
    """
    @property
    def type_of(self) -> str:
        return "icon"
