class ShapeColor:
    def __init__(self, shape: str = "", color: str = ""):
        if not isinstance(shape, str):
            raise TypeError("ERROR")
        self._shape = shape
        if not isinstance(color, str):
            raise TypeError("ERROR")
        self._color = color

    __slots__ = [
        "_shape",
        "_color"
    ]

    @property
    def shape(self):
        return self._shape

    @property
    def color(self):
        return self._color

    def set_attr(self, attr: str, value: str) -> None:
        if not isinstance(attr, str):
            raise TypeError("ERROR")
        if not isinstance(value, str):
            raise TypeError("ERROR")
        if f"_{attr}" in self.__slots__:
            setattr(self, f"_{attr}", value)
            return
        raise AttributeError("ERROR")


# a = ShapeColor(shape="1", color="2")
# a.set_attr(attr="shape", value="3")
# print(a.shape)
