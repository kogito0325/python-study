from color import WHITE
from objects import Rectangle


class Portal(Rectangle):
    def __init__(self, x=1000, y=400, w=100, h=200, color=WHITE):
        super().__init__(x, y, w, h, color)

    def tick(self):
        pass
