from math import atan2, cos, sin

from color import BLACK
from globals import Global
from objects import Rectangle, Player


class Enemy(Rectangle):
    SPEED = Player.SPEED * 0.8

    def __init__(self, x: int, y: int, target: Player):
        super().__init__(x, y, w=Player.SIZE, h=Player.SIZE, color=BLACK)

        self.target = target

    def tick(self):
        theta = atan2(self.target.y - self.y, self.target.x - self.x)

        offset = Enemy.SPEED / Global.display.fps

        x_offset = cos(theta) * offset
        y_offset = sin(theta) * offset

        self.x += x_offset
        self.y += y_offset
