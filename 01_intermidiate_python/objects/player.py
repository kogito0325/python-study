from pygame.constants import K_w, K_a, K_s, K_d

from util import limit
from color import ORANGE
from globals import Global
from objects import Rectangle


class Player(Rectangle):
    SIZE = 30
    SPEED = 1000  # px / s

    def __init__(self, x: int, y: int):
        super().__init__(x, y, w=Player.SIZE, h=Player.SIZE, color=ORANGE)

    def tick(self):
        offset = Player.SPEED / Global.display.fps

        if Global.keyboard.is_pressed(K_w):
            self.y -= offset
        if Global.keyboard.is_pressed(K_a):
            self.x -= offset
        if Global.keyboard.is_pressed(K_s):
            self.y += offset
        if Global.keyboard.is_pressed(K_d):
            self.x += offset

        self.x = limit(self.x, 0, Global.display.width - self.width)
        self.y = limit(self.y, 0, Global.display.height - self.height)
