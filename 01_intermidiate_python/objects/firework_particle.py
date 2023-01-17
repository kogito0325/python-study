from random import randint, random
from time import time

from color import RED, YELLOW
from globals import Global
from objects import Rectangle
from util import linear_interpolation, limit


class FireworkParticle(Rectangle):
    START_COLOR = YELLOW
    END_COLOR = RED

    GRAVITATIONAL_ACCELERATION = 1000
    PARTICLE_AMOUNT = 30

    def __init__(self, x: int, y: int, object_manager):
        size = randint(2, 5)
        super().__init__(x, y, size, size, FireworkParticle.START_COLOR)

        self.object_manager = object_manager

        self.x_velocity = (random() * 2 - 1) * 500
        self.y_velocity = (random() * 2 - 1) * 500 - 200

        self.animation_start = time()

    def tick(self):
        self.y_velocity += FireworkParticle.GRAVITATIONAL_ACCELERATION / Global.display.fps

        self.x += self.x_velocity / Global.display.fps
        self.y += self.y_velocity / Global.display.fps

        animation_duration = time() - self.animation_start
        red = limit(linear_interpolation(animation_duration, 0, 1.5,
                                         FireworkParticle.START_COLOR[0], FireworkParticle.END_COLOR[0]), 0, 255)
        green = limit(linear_interpolation(animation_duration, 0, 1.5,
                                           FireworkParticle.START_COLOR[1], FireworkParticle.END_COLOR[1]), 0, 255)
        blue = limit(linear_interpolation(animation_duration, 0, 1.5,
                                          FireworkParticle.START_COLOR[2], FireworkParticle.END_COLOR[2]), 0, 255)

        self.color = (red, green, blue)

        if self.y >= Global.display.height:
            self.object_manager.remove(self)
