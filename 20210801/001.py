import ctypes
import math
import time

import pygame  # 설치한 모듈

pygame.init()


class Color:
    BACKGROUND_COLOR = (3, 247, 229)


class Basis:
    running = True
    user32 = ctypes.windll.user32
    pixel_size = user32.GetSystemMetrics(1) // 9
    width, height = pixel_size * 8, pixel_size * 8
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
        Timing.previous_time = now


class Rect0:
    x, y = Basis.pixel_size, Basis.pixel_size
    size = (Basis.pixel_size * 6, Basis.pixel_size * 6)
    color = (7, 187, 173)


class Rect1:
    x, y = Basis.pixel_size, Basis.pixel_size * 2
    dx, dy = x, y
    speed = Basis.pixel_size * 8
    size = (Basis.pixel_size * 2, Basis.pixel_size * 2)
    color = (0, 0, 0)
    moving = [False, False, False, False]

    @staticmethod
    def handle(e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                Rect1.moving[0] = True
            elif e.key == pygame.K_a:
                Rect1.moving[1] = True
            elif e.key == pygame.K_s:
                Rect1.moving[2] = True
            elif e.key == pygame.K_d:
                Rect1.moving[3] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                Rect1.moving[0] = False
            elif e.key == pygame.K_a:
                Rect1.moving[1] = False
            elif e.key == pygame.K_s:
                Rect1.moving[2] = False
            elif e.key == pygame.K_d:
                Rect1.moving[3] = False

    @staticmethod
    def tick():
        if Rect1.x > Basis.width:
            Rect1.x -= Basis.width + Rect1.size[0]
        if Rect1.x < -Rect1.size[0]:
            Rect1.x += Basis.width + Rect1.size[0]
        if Rect1.y > Basis.height:
            Rect1.y -= Basis.height + Rect1.size[1]
        if Rect1.y < -Rect1.size[1]:
            Rect1.y += Basis.height + Rect1.size[1]

        offset1 = Rect1.speed / Timing.fps
        if Rect1.moving[0]:
            Rect1.y -= offset1
        if Rect1.moving[1]:
            Rect1.x -= offset1
        if Rect1.moving[2]:
            Rect1.y += offset1
        if Rect1.moving[3]:
            Rect1.x += offset1


class Rect2:
    x, y = Basis.pixel_size * 5, Basis.pixel_size * 2
    dx, dy = x, y
    speed = Basis.pixel_size * 8
    size = (Basis.pixel_size * 2, Basis.pixel_size * 2)
    color = (0, 0, 0)
    moving = [False, False, False, False]

    @staticmethod
    def handle(e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                Rect2.moving[0] = True
            elif e.key == pygame.K_LEFT:
                Rect2.moving[1] = True
            elif e.key == pygame.K_DOWN:
                Rect2.moving[2] = True
            elif e.key == pygame.K_RIGHT:
                Rect2.moving[3] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                Rect2.moving[0] = False
            elif e.key == pygame.K_LEFT:
                Rect2.moving[1] = False
            elif e.key == pygame.K_DOWN:
                Rect2.moving[2] = False
            elif e.key == pygame.K_RIGHT:
                Rect2.moving[3] = False

    @staticmethod
    def tick():
        if Rect2.x > Basis.width:
            Rect2.x -= Basis.width + Rect2.size[0]
        if Rect2.x < -Rect2.size[0]:
            Rect2.x += Basis.width + Rect2.size[0]
        if Rect2.y > Basis.height:
            Rect2.y -= Basis.height + Rect2.size[1]
        if Rect2.y < -Rect2.size[1]:
            Rect2.y += Basis.height + Rect2.size[1]

        offset2 = Rect2.speed / Timing.fps
        if Rect2.moving[0]:
            Rect2.y -= offset2
        if Rect2.moving[1]:
            Rect2.x -= offset2
        if Rect2.moving[2]:
            Rect2.y += offset2
        if Rect2.moving[3]:
            Rect2.x += offset2


class Rect3:
    x, y = Basis.pixel_size * 4, Basis.pixel_size * 5
    size = (Basis.pixel_size, Basis.pixel_size)
    color = (0, 0, 0)


def handle():
    for event in pygame.event.get():
        Basis.handle(event)
        Rect1.handle(event)
        Rect2.handle(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Rect1.x, Rect1.y = Rect1.dx, Rect1.dy
                Rect2.x, Rect2.y = Rect2.dx, Rect2.dy


def tick():
    Rect1.tick()
    Rect2.tick()


def render():
    Basis.display.fill(Color.BACKGROUND_COLOR)  # R, G, B

    pygame.draw.rect(Basis.display, Rect0.color, ((Rect0.x, Rect0.y), Rect0.size))
    pygame.draw.rect(Basis.display, Rect1.color, ((Rect1.x, Rect1.y), Rect1.size))
    pygame.draw.rect(Basis.display, Rect2.color, ((Rect2.x, Rect2.y), Rect2.size))
    pygame.draw.rect(Basis.display, Rect3.color, ((Rect3.x, Rect3.y), Rect3.size))

    pygame.display.flip()


if __name__ == '__main__':
    while Basis.running:
        Timing.handle()
        handle()
        tick()
        render()
