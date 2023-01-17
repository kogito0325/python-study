from random import randint

from globals import Global
from objects import Line, FireworkParticle


class FireworkBody(Line):
    def __init__(self, x: int, y: int, object_manager):
        super().__init__(x, y, x, y + 10, FireworkParticle.END_COLOR)

        self.object_manager = object_manager

        self.y_velocity = -randint(600, 1400)

    def tick(self):
        self.y_velocity += FireworkParticle.GRAVITATIONAL_ACCELERATION / Global.display.fps
        self.y += self.y_velocity / Global.display.fps
        self.y2 += self.y_velocity / Global.display.fps

        if self.y_velocity >= 0:
            for _ in range(FireworkParticle.PARTICLE_AMOUNT):
                self.object_manager.add(FireworkParticle(self.x, self.y, self.object_manager))
            self.object_manager.remove(self)
