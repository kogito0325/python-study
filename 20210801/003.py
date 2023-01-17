import math
import random
import time

import pygame

pygame.init()


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class Basis:
    running = True
    width, height = 1000, 800
    display = pygame.display.set_mode((width, height))

    @staticmethod
    def handle(e):
        if e.type == pygame.QUIT:  # X 버튼을 누름
            Basis.running = False


class Timing:
    previous_time = 0
    fps = 1

    @staticmethod
    def handle():
        now = time.time()
        try:
            Timing.fps = 1 / (now - Timing.previous_time)
        except ZeroDivisionError:
            Timing.fps = math.inf
        else:
            Timing.previous_time = now


class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0
        # 현재 마우스의 위치

        self.left = False
        self.right = False

    def handle(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            self.x, self.y = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.left = True
            elif event.button == 3:
                self.right = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.left = False
            elif event.button == 3:
                self.right = False


class Particle:
    GRAVITY = 5000

    def __init__(self, x: int, y: int):
        self.x = x
        self.dx = random.random() * 1000 - 500
        self.y = y
        self.dy = -(random.random() * 1000)
        self.size = random.randint(3, 8)
        self.color = Color.WHITE

    def tick(self):
        self.dy += Particle.GRAVITY / Timing.fps
        self.y += self.dy / Timing.fps
        self.x += self.dx / Timing.fps
        if self.y >= Basis.height:
            objects.remove(self)

    def render(self):
        pygame.draw.rect(Basis.display, self.color, ((self.x, self.y), (self.size,) * 2))


mouse = Mouse()
objects = []


def handle():
    for event in pygame.event.get():
        Basis.handle(event)
        mouse.handle(event)


def tick():
    if mouse.left or mouse.right:
        objects.append(Particle(mouse.x, mouse.y))

    for obj in objects:
        obj.tick()


def render():
    Basis.display.fill(Color.BLACK)  # R, G, B

    for obj in objects:
        obj.render()

    pygame.display.flip()


if __name__ == '__main__':
    while Basis.running:
        Timing.handle()
        handle()
        tick()
        render()
