from lab_python_oop.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, board: float,color: str = ''):
        super(Square, self).__init__(board, board,color)

