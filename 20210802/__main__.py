import pygame

from globals import Global
from color import Color
from display import Display
from mouse import Mouse

pygame.init()


class Main:
    def __init__(self):
        self.running = True

        Global.display = Display(1280, 720)
        Global.mouse = Mouse()
        Global.objects = []

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            Global.mouse.handle(event)

    @staticmethod
    def tick():
        Global.display.tick()
        Global.mouse.tick()

        for obj in Global.objects:
            obj.tick()

        Global.mouse.clear_status()
        print(len(Global.objects))

    @staticmethod
    def render():
        Global.display.window.fill(Color.BLACK)
        for obj in Global.objects:
            obj.render()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle()
            self.tick()
            self.render()


if __name__ == '__main__':
    main = Main()
    main.run()
