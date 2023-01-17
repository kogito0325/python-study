# advanced player.py
from pygame.constants import K_a, K_d, K_SPACE

from color import ORANGE
from globals import Global
from objects import Rectangle, Player
from util import limit


class AdvancedPlayer(Rectangle):
    GRAVITY = 2000
    SPEED = 500

    def __init__(self, x=100, y=300, w=30, h=30, color=ORANGE):
        super().__init__(x, y, w, h, color)

        self.dy = 0

    def jump(self):
        if self.y + self.height >= Global.display.height:
            self.dy = -1000

    def enter_portal(self):
        pass

    def tick(self):
        offset = AdvancedPlayer.SPEED / Global.display.fps

        self.dy += AdvancedPlayer.GRAVITY / Global.display.fps
        self.y += self.dy / Global.display.fps

        if Global.keyboard.is_pressed(K_a):
            self.x -= offset
        if Global.keyboard.is_pressed(K_d):
            self.x += offset
        if Global.keyboard.is_start(K_SPACE):
            self.jump()

        self.x = limit(self.x, 0, Global.display.width - self.width)
        self.y = limit(self.y, 0, Global.display.height - self.height)

