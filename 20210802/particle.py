import random
import pygame

from globals import Global


class Particle:
    g = 5000

    def __init__(self, x: int, y: int, color: tuple):
        self.x = x
        self.y = y
        self.color = color

        self.size = random.randint(2, 15)

        self.dx = (random.random() * 2 - 1) * 500
        self.dy = (random.random() * 2 - 1.5) * 500

    def tick(self):
        self.dy += Particle.g / Global.display.fps

        self.x += self.dx / Global.display.fps
        self.y += self.dy / Global.display.fps

        if self.y >= Global.display.height:
            Global.objects.remove(self)

    def render(self):
        pygame.draw.rect(Global.display.window, self.color, ((self.x, self.y), (self.size, self.size)))
