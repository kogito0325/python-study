from math import inf
from time import time

from pygame import display


class Display:
    def __init__(self, width, height, caption):
        self.width, self.height = width, height

        display.set_caption(caption)
        self.window = display.set_mode((self.width, self.height))

        self._previous_time = time()
        self.fps = 1

    def tick(self):
        now = time()
        try:
            self.fps = 1 / (now - self._previous_time)
        except ZeroDivisionError:
            self.fps = inf
        else:
            self._previous_time = now
