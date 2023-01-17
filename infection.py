import math

import pygame
import time
import random

pygame.init()

class Game:
    class display:
        width = 1280
        height = 720

        fps = 60

        loop_delay = 0

    window = pygame.display.set_mode((display.width, display.height))

    exit = False

class Keyboard:
    lalt = False
    ralt = False

class Cursor:
    position = pygame.mouse.get_pos()
    ppressed = pressed = pygame.mouse.get_pressed()

    fpressed = list(pressed)

class Color:
    white = (255, 255, 255)
    gray = (127, 127, 127)
    black = (0, 0, 0)

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tick(self):
        pass

    def render(self):
        pass

objects = []

class Plate(GameObject):
    def __init__(self, width, height, colors):
        super().__init__(0, 0)

        self.width = width
        self.height = height

        self.colors = colors

        self.size = (Game.display.width / self.width, Game.display.height / self.height)

        self.board = []
        for y in range(self.height):
            self.board.append([])
            for x in range(self.width):
                self.board[y].append(2)
        # print(self.board)

    def tick(self):
        if Cursor.fpressed[0]:
            x, y = self.get_grid_position()
            self.board[y][x] = 0
        elif Cursor.fpressed[2]:
            x, y = self.get_grid_position()
            self.board[y][x] = 1

        if self.statistics()[0] == 0 and self.statistics()[1] == 0:
            return

        # self.alg1()
        self.alg2()

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != 2:
                    pygame.draw.rect(Game.window, self.colors[self.board[y][x]], ((self.size[0] * x, self.size[1] * y), self.size))

    def alg1(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.board[y][x] != 2:
                break
        d = random.randint(0, 3)

        try:
            if self.board[x][y] == 2:
                return
        except:
            return

        if d == 0 and y != 0:
            self.board[y-1][x] = self.board[y][x]
        elif d == 1 and x != 0:
            self.board[y][x-1] = self.board[y][x]
        elif d == 2 and y != self.height - 1:
            self.board[y+1][x] = self.board[y][x]
        elif d == 3 and x != self.width - 1:
            self.board[y][x+1] = self.board[y][x]

    def alg2(self):
        for y in range(self.height):
            for x in range(self.width):
                if round(random.random() * 1) != 0:
                    continue
                if self.board[y][x] == 2:
                    continue

                d = round(random.random() * 3.785 + 0.5) - 1

                if d == 0 and y != 0:
                    self.board[y - 1][x] = self.board[y][x]
                elif d == 1 and x != 0:
                    self.board[y][x - 1] = self.board[y][x]
                elif d == 2 and y != self.height - 1:
                    self.board[y + 1][x] = self.board[y][x]
                elif d == 3 and x != self.width - 1:
                    self.board[y][x + 1] = self.board[y][x]

    def get_grid_position(self):
        pos = Cursor.position
        return int(pos[0] // self.size[0]), int(pos[1] // self.size[1])

    def statistics(self):
        result = [0, 0, 0]

        for y in range(self.height):
            for x in range(self.width):
                result[self.board[y][x]] += 1

        return result

a = Plate(128, 72, (Color.black, Color.white))
a.board[a.height-1][0] = 0
a.board[0][a.width-1] = 1
objects.append(a)

while not Game.exit:
    start = time.time()

    Cursor.position = pygame.mouse.get_pos()
    Cursor.pressed = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                Keyboard.lalt = True
            elif event.key == pygame.K_RALT:
                Keyboard.ralt = True
            elif event.key == pygame.K_F4:
                if Keyboard.lalt or Keyboard.ralt:
                    Game.exit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT:
                Keyboard.lalt = False
            elif event.key == pygame.K_RALT:
                Keyboard.ralt = False

    for i in range(3):
        Cursor.fpressed[i] = not Cursor.ppressed[i] and Cursor.pressed[i]

    for obj in objects:
        obj.tick()

    Game.window.fill(Color.gray)
    for obj in objects:
        obj.render()
    pygame.display.flip()

    delta = 0
    while time.time() - start < 1 / Game.display.fps:
        delta += 1
    Game.display.loop_delay = delta * Game.display.fps

    a = objects[0].statistics()
    print(1 - abs(a[0] / a[1] - 1))
pygame.quit()
exit()
