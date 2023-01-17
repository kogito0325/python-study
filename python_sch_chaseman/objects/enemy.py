from math import atan2, cos, sin

from color import Color
from globals import Global
from objects import Rectangle, Player


class Enemy(Rectangle):
    SPEED = 800

    def __init__(self, x: int, y: int, target: Player):
        super().__init__(x, y, 20, 20, Color.BLACK)

        self.target = target

    def tick(self):
        theta = atan2(self.target.y - self.y, self.target.x - self.x)
        offset = Enemy.SPEED / Global.display.fps
        x_offset = offset * cos(theta)
        y_offset = offset * sin(theta)

        self.x += x_offset
        self.y += y_offset
