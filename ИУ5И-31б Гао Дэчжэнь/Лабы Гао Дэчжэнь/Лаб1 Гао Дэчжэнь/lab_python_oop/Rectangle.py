from lab_python_oop.MetaClass.GeometricShap import GeometricShape
from lab_python_oop.MetaClass.ShapeColor import ShapeColor


class Rectangle(GeometricShape):

    _SHAPE = None

    def __init__(self, width: float,height: float, color: str):
        self.width = width
        self.height = height
        self._shape_color = ShapeColor(shape=f"{self.__class__.__name__}", color=color)

    def __repr__(self):
        return "<{} object at {} width: {}, height: {}, color: {}>".format(self.__class__.__name__,
                                                                           str(hex(id(self))),
                                                                           str(self.width),
                                                                           str(self.height),
                                                                           str(self.color))

    def count_square(self, *args, **kwargs) -> float:
        return self.width * self.height

    def __new__(cls, *args, **kwargs):
        cls._shape_init()
        return object.__new__(cls)
    @property
    def color(self):
        return self._shape_color.color

    @classmethod
    def _shape_init(cls):
        cls._SHAPE = cls.__name__

    @classmethod
    def shape(cls):
        return cls._SHAPE



