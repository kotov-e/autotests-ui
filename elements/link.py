from elements.base_element import BaseElement


class Link(BaseElement):
    """
    Класс элемента link
    """

    @property
    def type_of(self) -> str:
        return "link"
