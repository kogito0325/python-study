import math
import time

import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 1280, 720


def center(big, small) -> float:
    return (big - small) // 2


window = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

# TIMING
previous_time = 0

# MOUSE
mouse_x = 0
mouse_y = 0

# RECT
rect_size = (100, 100)
rect_x = center(WIDTH, rect_size[0])
rect_y = center(HEIGHT, rect_size[1])
rect_color = RED
rect_speed = 1000  # px/s
rect_moving = [False, False, False, False]

# IMAGE
IMAGE_PATH = 'res/image/thumbnail.png'
image_surface = pygame.image.load(IMAGE_PATH)
image_surface = pygame.transform.smoothscale(image_surface,
                                             (image_surface.get_width() // 4, image_surface.get_height() // 4))
image_width = image_surface.get_width()
image_height = image_surface.get_height()
image_x = 0
image_y = 0

# TEXT
"""
사각형의 위치
화면의 아래 중앙
파란색
"""
FONT_PATH = 'res/font/Pretendard-Bold.otf'
font_size = 48
text_font = pygame.font.Font(FONT_PATH, font_size)
text_color = BLUE
text_surface = text_font.render('0, 0', True, text_color)
text_x = center(WIDTH, text_surface.get_width())
text_y = HEIGHT / 5 * 4

while running:
    now = time.time()
    try:
        fps = 1 / (now - previous_time)
    except ZeroDivisionError:
        fps = math.inf
    previous_time = now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect_moving[0] = True
            elif event.key == pygame.K_a:
                rect_moving[1] = True
            elif event.key == pygame.K_s:
                rect_moving[2] = True
            elif event.key == pygame.K_d:
                rect_moving[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rect_moving[0] = False
            elif event.key == pygame.K_a:
                rect_moving[1] = False
            elif event.key == pygame.K_s:
                rect_moving[2] = False
            elif event.key == pygame.K_d:
                rect_moving[3] = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    if rect_moving[0]:
        rect_y -= rect_speed / fps
    if rect_moving[1]:
        rect_x -= rect_speed / fps
    if rect_moving[2]:
        rect_y += rect_speed / fps
    if rect_moving[3]:
        rect_x += rect_speed / fps

    image_x, image_y = mouse_x, mouse_y

    text_surface = text_font.render(f'{int(rect_x)}, {int(rect_y)}', True, text_color)
    text_x = center(WIDTH, text_surface.get_width())

    window.fill(WHITE)

    window.blit(image_surface, (image_x - image_width / 2, image_y - image_height / 2))
    pygame.draw.rect(window, rect_color, ((rect_x, rect_y), rect_size))
    window.blit(text_surface, (text_x, text_y))

    pygame.display.flip()

pygame.quit()
