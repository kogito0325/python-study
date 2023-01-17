from pygame import Surface
from pygame.font import Font as PygameFont


class Font:
    def __init__(self, path: str, size: int, color: tuple):
        self.path = path
        self.size = size
        self.color = color

        self.font = PygameFont(self.path, self.size)

    def render(self, text: str) -> Surface:
        return self.font.render(text, True, self.color)
