from font import Font
from globals import Global
from objects import Object


class Text(Object):
    def __init__(self, x: int, y: int, text: str, font: Font):
        super().__init__(x, y)

        self.text = text
        self.font = font

        self.surface = self.font.render(self.text)

    def render(self):
        Global.display.window.blit(self.surface, (self.x, self.y))
