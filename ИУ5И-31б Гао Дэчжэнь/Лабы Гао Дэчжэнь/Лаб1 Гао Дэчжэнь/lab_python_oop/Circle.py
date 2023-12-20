import math

from lab_python_oop.MetaClass.GeometricShap import GeometricShape
from lab_python_oop.MetaClass.ShapeColor import ShapeColor


class Circle(GeometricShape):

    _SHAPE = None

    def __init__(self, radius: float, color: str = ""):
        self.radius = radius
        self._shape_color = ShapeColor(shape="Circle", color=color)

    def __repr__(self):
        return "<{} object at {}, radius: {}, color: {}>".format(self.__class__.__name__,
                                                                 str(hex(id(self))),
                                                                 str(self.radius),
                                                                 str(self.color))

    def count_square(self, *args, **kwargs) -> float:
        return math.pi * self.radius ** 2

    @property
    def color(self):
        return self._shape_color.color

    @classmethod
    def _shape_init(cls):
        cls._SHAPE = cls.__name__

    def __new__(cls, *args, **kwargs):
        cls._shape_init()
        return object.__new__(cls)

    @classmethod
    def shape(cls):
        return cls.__name__
