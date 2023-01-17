from objects import Object


class Rectangle(Object):
    def __init__(self, x: int, y: int, w: int, h: int, color: tuple):
        super().__init__(x, y)

        self.width = w
        self.height = h
        self.color = color

