# rectangle.py

from pygame import draw

from objects import Object
from globals import Global


class Rectangle(Object):
    def __init__(self, x: int, y: int, w: int, h: int, color: tuple):
        super().__init__(x, y)

        self.width = w
        self.height = h
        self.color = color

    def render(self):
        draw.rect(Global.display.window, self.color, ((self.x, self.y), (self.width, self.height)))
