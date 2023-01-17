import math
import time

import pygame

pygame.init()

BACKGROUND_COLOR = (3, 247, 229)

running = True

width, height = 720, 720
display = pygame.display.set_mode((width, height))

previous_time = 0

rect0_x, rect0_y = 90, 90
rect0_size = (540, 540)
rect0_color = (7, 187, 173)

rect1_x, rect1_y = 90, 180
d1x, d1y = rect1_x, rect1_y
rect1_speed = 720
rect1_size = (180, 180)
rect1_color = (0, 0, 0)
rect1_moving = [False, False, False, False]

rect2_x, rect2_y = 450, 180
d2x, d2y = rect2_x, rect2_y
rect2_speed = 720
rect2_size = (180, 180)
rect2_color = (0, 0, 0)
rect2_moving = [False, False, False, False]

rect3_x, rect3_y = 360, 450
rect3_size = (90, 90)
rect3_color = (0, 0, 0)


def handle():
    global running, rect1_x, rect1_y, rect2_x, rect2_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # X 버튼을 누름
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect1_moving[0] = True
            elif event.key == pygame.K_a:
                rect1_moving[1] = True
            elif event.key == pygame.K_s:
                rect1_moving[2] = True
            elif event.key == pygame.K_d:
                rect1_moving[3] = True
            elif event.key == pygame.K_UP:
                rect2_moving[0] = True
            elif event.key == pygame.K_LEFT:
                rect2_moving[1] = True
            elif event.key == pygame.K_DOWN:
                rect2_moving[2] = True
            elif event.key == pygame.K_RIGHT:
                rect2_moving[3] = True
            if event.key == pygame.K_r:
                rect1_x, rect1_y = d1x, d1y
                rect2_x, rect2_y = d2x, d2y
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rect1_moving[0] = False
            elif event.key == pygame.K_a:
                rect1_moving[1] = False
            elif event.key == pygame.K_s:
                rect1_moving[2] = False
            elif event.key == pygame.K_d:
                rect1_moving[3] = False
            if event.key == pygame.K_UP:
                rect2_moving[0] = False
            elif event.key == pygame.K_LEFT:
                rect2_moving[1] = False
            elif event.key == pygame.K_DOWN:
                rect2_moving[2] = False
            elif event.key == pygame.K_RIGHT:
                rect2_moving[3] = False


def tick():
    global rect1_x, rect1_y, rect2_x, rect2_y

    if rect1_x > width:
        rect1_x -= width + rect1_size[0]
    if rect1_x < -rect1_size[0]:
        rect1_x += width + rect1_size[0]
    if rect1_y > height:
        rect1_y -= height + rect1_size[1]
    if rect1_y < -rect1_size[1]:
        rect1_y += height + rect1_size[1]

    if rect2_x > width:
        rect2_x -= width + rect2_size[0]
    if rect2_x < -rect2_size[0]:
        rect2_x += width + rect2_size[0]
    if rect2_y > height:
        rect2_y -= height + rect2_size[1]
    if rect2_y < -rect2_size[1]:
        rect2_y += height + rect2_size[1]

    offset1 = rect1_speed / fps
    if rect1_moving[0]:
        rect1_y -= offset1
    if rect1_moving[1]:
        rect1_x -= offset1
    if rect1_moving[2]:
        rect1_y += offset1
    if rect1_moving[3]:
        rect1_x += offset1

    offset2 = rect2_speed / fps
    if rect2_moving[0]:
        rect2_y -= offset2
    if rect2_moving[1]:
        rect2_x -= offset2
    if rect2_moving[2]:
        rect2_y += offset2
    if rect2_moving[3]:
        rect2_x += offset2


def render():
    display.fill(BACKGROUND_COLOR)  # R, G, B

    pygame.draw.rect(display, rect0_color, ((rect0_x, rect0_y), rect0_size))
    pygame.draw.rect(display, rect1_color, ((rect1_x, rect1_y), rect1_size))
    pygame.draw.rect(display, rect2_color, ((rect2_x, rect2_y), rect2_size))
    pygame.draw.rect(display, rect3_color, ((rect3_x, rect3_y), rect3_size))

    pygame.display.flip()


while running:
    now = time.time()
    try:
        fps = 1 / (now - previous_time)
    except ZeroDivisionError:
        fps = math.inf
    previous_time = now

    handle()
    tick()
    render()

pygame.quit()
