from lab_python_oop.Square import Square
from lab_python_oop.Circle import Circle
from lab_python_oop.Rectangle import Rectangle


width = 21
height = 28
blue_rectangle = Rectangle(width=width, height=height, color='blue')
circle = Circle(radius=21, color='green')
square = Square(board=21, color='red')


def test(obj):
    print(obj.count_square())


if"__main__" == __name__:
    test(blue_rectangle)
    test(circle)
    test(square)