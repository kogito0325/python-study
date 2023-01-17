from pygame import draw

from objects import Object
from globals import Global


class Line(Object):
    def __init__(self, x: int, y: int, x2: int, y2: int, color: tuple, width: int = 1):
        """
        화면 상에 선을 나타내는 오브젝트

        :param x: 시작점 x좌표
        :param y: 시작점 y좌표
        :param x2: 끝점 x좌표
        :param y2: 끝점 y좌표
        :param color: 선 색상
        :param width: 선 굵기
        """
        super().__init__(x, y)

        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def set_end_pos(self, x, y) -> 'Line':
        self.x2 = x
        self.y2 = y
        return self

    def render(self):
        draw.line(Global.display.window, self.color, (self.x, self.y), (self.x2, self.y2), self.width)
