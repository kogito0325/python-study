import math
import time

import pygame

pygame.init()


class Util:
    @staticmethod
    def center(big, small) -> float:
        return (big - small) // 2


class Color:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)


class Basis:
    WIDTH, HEIGHT = 1280, 720
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    @staticmethod
    def handle(e):
        if e.type == pygame.QUIT:
            Basis.running = False

    @staticmethod
    def render():
        Basis.window.fill(Color.WHITE)


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


class Mouse:
    x = 0
    y = 0

    @staticmethod
    def handle(e):
        if e.type == pygame.MOUSEMOTION:
            Mouse.x, Mouse.y = e.pos


class Rect:
    size = (100, 100)
    x = Util.center(Basis.WIDTH, size[0])
    y = Util.center(Basis.HEIGHT, size[1])
    color = Color.RED
    speed = 1000  # px/s
    moving = [False, False, False, False]

    @staticmethod
    def handle(e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                Rect.moving[0] = True
            elif e.key == pygame.K_a:
                Rect.moving[1] = True
            elif e.key == pygame.K_s:
                Rect.moving[2] = True
            elif e.key == pygame.K_d:
                Rect.moving[3] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                Rect.moving[0] = False
            elif e.key == pygame.K_a:
                Rect.moving[1] = False
            elif e.key == pygame.K_s:
                Rect.moving[2] = False
            elif e.key == pygame.K_d:
                Rect.moving[3] = False

    @staticmethod
    def tick():
        if Rect.moving[0]:
            Rect.y -= Rect.speed / Timing.fps
        if Rect.moving[1]:
            Rect.x -= Rect.speed / Timing.fps
        if Rect.moving[2]:
            Rect.y += Rect.speed / Timing.fps
        if Rect.moving[3]:
            Rect.x += Rect.speed / Timing.fps

    @staticmethod
    def render():
        pygame.draw.rect(Basis.window, Rect.color, ((Rect.x, Rect.y), Rect.size))


class Image:
    path = 'res/image/thumbnail.png'
    surface = pygame.image.load(path)
    surface = pygame.transform.smoothscale(surface, (surface.get_width() // 4, surface.get_height() // 4))
    width = surface.get_width()
    height = surface.get_height()
    image_x = 0
    image_y = 0

    @staticmethod
    def tick():
        Image.image_x, Image.image_y = Mouse.x, Mouse.y

    @staticmethod
    def render():
        Basis.window.blit(Image.surface,
                          (Image.image_x - Image.width / 2, Image.image_y - Image.height / 2))


class Text:
    """
    사각형의 위치
    화면의 아래 중앙
    파란색
    """
    path = 'res/font/YINP05.TTF'  # 'res/font/Pretendard-Bold.otf'
    size = 48
    font = pygame.font.Font(path, size)
    color = Color.BLUE
    surface = font.render('0, 0', True, color)
    x = Util.center(Basis.WIDTH, surface.get_width())
    y = Basis.HEIGHT / 5 * 4

    @staticmethod
    def tick():
        Text.surface = Text.font.render(f'{int(Rect.x)}, {int(Rect.y)}', True, Text.color)
        Text.x = Util.center(Basis.WIDTH, Text.surface.get_width())

    @staticmethod
    def render():
        Basis.window.blit(Text.surface, (Text.x, Text.y))


while Basis.running:
    Timing.handle()

    for event in pygame.event.get():
        Basis.handle(event)
        Rect.handle(event)
        Mouse.handle(event)

    Rect.tick()
    Image.tick()
    Text.tick()

    Basis.render()
    Image.render()
    Rect.render()
    Text.render()

    pygame.display.flip()

pygame.quit()
