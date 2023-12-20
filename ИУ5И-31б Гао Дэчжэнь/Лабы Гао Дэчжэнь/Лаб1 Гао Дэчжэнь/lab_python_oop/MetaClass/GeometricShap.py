from abc import abstractmethod, ABCMeta


class GeometricShape(metaclass=ABCMeta):
    """abstractmethod for class Geometric Shape """

    #count square recive
    @abstractmethod
    def count_square(self, *args, **kwargs) -> float:
        pass