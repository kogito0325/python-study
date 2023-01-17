import random
import pygame

from color import Color
from basis import Basis


class Particle:
    gravity = 2000

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.size = random.randint(2, 8)
        self.color = Color.BLACK

        self.dx = (random.random() * 2 - 1) * 300
        self.dy = (random.random() * 2 - 1) * 300

    def tick(self):
        self.x += self.dx / Basis.fps
        self.dy += Particle.gravity / Basis.fps
        self.y += self.dy / Basis.fps

    def render(self):
        pygame.draw.rect(Basis.window, self.color, ((self.x, self.y), (self.size, self.size)))
