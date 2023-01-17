from pygame import image

from globals import Global
from objects import Object


class Image(Object):
    def __init__(self, x: int, y: int, path: str):
        super().__init__(x, y)

        self.path = path

        self.surface = image.load(self.path)

    def render(self):
        Global.display.window.blit(self.surface, (self.x, self.y))
