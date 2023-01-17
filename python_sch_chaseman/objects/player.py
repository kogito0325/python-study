from pygame.constants import K_w, K_a, K_s, K_d

from color import Color
from globals import Global
from objects import Rectangle
from util import limit


class Player(Rectangle):
    SPEED = 1000

    def __init__(self, x: int, y: int):
        super().__init__(x, y, 20, 20, Color.ORANGE)

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
        # if self.x < 0:
        #     self.x = 0
        # elif self.x > Global.display.width - self.width:
        #     self.x = Global.display.width - self.width
        # if self.y < 0:
        #     self.y = 0
        # elif self.y > Global.display.height - self.height:
        #     self.y = Global.display.height - self.height
