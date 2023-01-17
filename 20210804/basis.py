import math
import time

import pygame


class Basis:
    width = 1000
    height = 800
    running = True

    fps = 1
    _previous_time = 0

    window = pygame.display.set_mode((width, height))

    @staticmethod
    def tick():
        now = time.time()
        try:
            Basis.fps = 1 / (now - Basis._previous_time)
        except ZeroDivisionError:
            Basis.fps = math.inf
        else:
            Basis._previous_time = now
