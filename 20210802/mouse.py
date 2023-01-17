import pygame

from globals import Global
from particle import Particle
from color import Color


class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.left = False
        self.wheel = False
        self.right = False

        self.left_start = False

    def handle(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                self.left = True
                self.left_start = True
            if event.button == pygame.BUTTON_MIDDLE:
                self.wheel = True
            if event.button == pygame.BUTTON_RIGHT:
                self.right = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                self.left = False
            if event.button == pygame.BUTTON_MIDDLE:
                self.wheel = False
            if event.button == pygame.BUTTON_RIGHT:
                self.right = False
        elif event.type == pygame.MOUSEMOTION:
            self.x, self.y = event.pos

    def clear_status(self):
        if self.left_start:
            self.left_start = False

    def tick(self):
        if self.left_start:
            for _ in range(20):
                Global.objects.append(Particle(self.x, self.y, Color.WHITE))
