from elements.base_element import BaseElement


class Image(BaseElement):
    """
    Класс элемента image
    """

    @property
    def type_of(self) -> str:
        return "image"
