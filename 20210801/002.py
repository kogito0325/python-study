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


class Rect:
    SPEED = Basis.pixel_size * 8

    def __init__(self, x: int, y: int, size: int, color: tuple, keys: tuple = tuple()):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.keys = keys

        self.moving = [False, False, False, False]

    def handle(self, e):
        if self.keys:
            if e.type == pygame.KEYDOWN:
                for i in range(4):
                    if e.key == self.keys[i]:
                        self.moving[i] = True
                        break
            elif e.type == pygame.KEYUP:
                for i in range(4):
                    if e.key == self.keys[i]:
                        self.moving[i] = False
                        break

    def tick(self):
        if self.keys:
            if self.x > Basis.width:
                self.x -= Basis.width + self.size
            if self.x < -self.size:
                self.x += Basis.width + self.size
            if self.y > Basis.height:
                self.y -= Basis.height + self.size
            if self.y < -self.size:
                self.y += Basis.height + self.size

            offset = Rect.SPEED / Timing.fps
            if self.moving[0]:
                self.y -= offset
            if self.moving[1]:
                self.x -= offset
            if self.moving[2]:
                self.y += offset
            if self.moving[3]:
                self.x += offset

    def render(self):
        pygame.draw.rect(Basis.display, self.color, ((self.x, self.y), (self.size, self.size)))

# class Rect0:
#     x, y = Basis.pixel_size, Basis.pixel_size
#     size = (Basis.pixel_size * 6, Basis.pixel_size * 6)
#     color = (7, 187, 173)
#
#
# class Rect1:
#     x, y = Basis.pixel_size, Basis.pixel_size * 2
#     dx, dy = x, y
#     speed = Basis.pixel_size * 8
#     size = (Basis.pixel_size * 2, Basis.pixel_size * 2)
#     color = (0, 0, 0)
#     moving = [False, False, False, False]
#
#     @staticmethod
#     def handle(e):
#         if e.type == pygame.KEYDOWN:
#             if e.key == pygame.K_w:
#                 Rect1.moving[0] = True
#             elif e.key == pygame.K_a:
#                 Rect1.moving[1] = True
#             elif e.key == pygame.K_s:
#                 Rect1.moving[2] = True
#             elif e.key == pygame.K_d:
#                 Rect1.moving[3] = True
#         elif e.type == pygame.KEYUP:
#             if e.key == pygame.K_w:
#                 Rect1.moving[0] = False
#             elif e.key == pygame.K_a:
#                 Rect1.moving[1] = False
#             elif e.key == pygame.K_s:
#                 Rect1.moving[2] = False
#             elif e.key == pygame.K_d:
#                 Rect1.moving[3] = False
#
#     @staticmethod
#     def tick():
#         if Rect1.x > Basis.width:
#             Rect1.x -= Basis.width + Rect1.size[0]
#         if Rect1.x < -Rect1.size[0]:
#             Rect1.x += Basis.width + Rect1.size[0]
#         if Rect1.y > Basis.height:
#             Rect1.y -= Basis.height + Rect1.size[1]
#         if Rect1.y < -Rect1.size[1]:
#             Rect1.y += Basis.height + Rect1.size[1]
#
#         offset1 = Rect1.speed / Timing.fps
#         if Rect1.moving[0]:
#             Rect1.y -= offset1
#         if Rect1.moving[1]:
#             Rect1.x -= offset1
#         if Rect1.moving[2]:
#             Rect1.y += offset1
#         if Rect1.moving[3]:
#             Rect1.x += offset1
#
#
# class Rect2:
#     x, y = Basis.pixel_size * 5, Basis.pixel_size * 2
#     dx, dy = x, y
#     speed = Basis.pixel_size * 8
#     size = (Basis.pixel_size * 2, Basis.pixel_size * 2)
#     color = (0, 0, 0)
#     moving = [False, False, False, False]
#
#     @staticmethod
#     def handle(e):
#         if e.type == pygame.KEYDOWN:
#             if e.key == pygame.K_UP:
#                 Rect2.moving[0] = True
#             elif e.key == pygame.K_LEFT:
#                 Rect2.moving[1] = True
#             elif e.key == pygame.K_DOWN:
#                 Rect2.moving[2] = True
#             elif e.key == pygame.K_RIGHT:
#                 Rect2.moving[3] = True
#         elif e.type == pygame.KEYUP:
#             if e.key == pygame.K_UP:
#                 Rect2.moving[0] = False
#             elif e.key == pygame.K_LEFT:
#                 Rect2.moving[1] = False
#             elif e.key == pygame.K_DOWN:
#                 Rect2.moving[2] = False
#             elif e.key == pygame.K_RIGHT:
#                 Rect2.moving[3] = False
#
#     @staticmethod
#     def tick():
#         if Rect2.x > Basis.width:
#             Rect2.x -= Basis.width + Rect2.size[0]
#         if Rect2.x < -Rect2.size[0]:
#             Rect2.x += Basis.width + Rect2.size[0]
#         if Rect2.y > Basis.height:
#             Rect2.y -= Basis.height + Rect2.size[1]
#         if Rect2.y < -Rect2.size[1]:
#             Rect2.y += Basis.height + Rect2.size[1]
#
#         offset2 = Rect2.speed / Timing.fps
#         if Rect2.moving[0]:
#             Rect2.y -= offset2
#         if Rect2.moving[1]:
#             Rect2.x -= offset2
#         if Rect2.moving[2]:
#             Rect2.y += offset2
#         if Rect2.moving[3]:
#             Rect2.x += offset2
#
#
# class Rect3:
#     x, y = Basis.pixel_size * 4, Basis.pixel_size * 5
#     size = (Basis.pixel_size, Basis.pixel_size)
#     color = (0, 0, 0)


objects = [
    Rect(Basis.pixel_size, Basis.pixel_size, Basis.pixel_size * 6, (7, 187, 173)),
    Rect(Basis.pixel_size, Basis.pixel_size * 2, Basis.pixel_size * 2, (0, 0, 0),
         (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)),
    Rect(Basis.pixel_size * 5, Basis.pixel_size * 2, Basis.pixel_size * 2, (0, 0, 0),
         (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT)),
    Rect(Basis.pixel_size * 4, Basis.pixel_size * 5, Basis.pixel_size, (0, 0, 0))
]


def handle():
    for event in pygame.event.get():
        Basis.handle(event)
        for obj in objects:
            obj.handle(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                objects[1].x, objects[1].y = Basis.pixel_size, Basis.pixel_size * 2
                objects[2].x, objects[2].y = Basis.pixel_size * 5, Basis.pixel_size * 2


def tick():
    for obj in objects:
        obj.tick()


def render():
    Basis.display.fill(Color.BACKGROUND_COLOR)  # R, G, B

    for obj in objects:
        obj.render()

    pygame.display.flip()


if __name__ == '__main__':
    while Basis.running:
        Timing.handle()
        handle()
        tick()
        render()
