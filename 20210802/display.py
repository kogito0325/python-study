import pygame
import time
import math


class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.display.set_caption('Particle')
        pygame.display.set_icon(pygame.image.load('res/icon/icon.jpg'))
        self.window = pygame.display.set_mode((self.width, self.height))

        self.fps = 1
        self._previous_time = 0

    def tick(self):
        now = time.time()
        try:
            self.fps = 1 / (now - self._previous_time)
        except ZeroDivisionError:
            self.fps = math.inf
        else:
            self._previous_time = now
