import pygame

from basis import Basis
from color import Color
from mouse import Mouse
from particle import Particle

pygame.init()


class Main:
    objects = []
    mouse = Mouse()

    @staticmethod
    def tick():
        Basis.tick()
        for obj in Main.objects:
            obj.tick()
            if obj.y >= Basis.height:
                Main.objects.remove(obj)

    @staticmethod
    def render():
        Basis.window.fill(Color.WHITE)
        for obj in Main.objects:
            obj.render()

        pygame.display.flip()

    @staticmethod
    def run():
        while Basis.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Basis.running = False
                Main.mouse.handle(event)
            if Main.mouse.clicked:
                Main.objects.append(Particle(Main.mouse.x, Main.mouse.y))
            Main.tick()
            Main.render()
        pygame.quit()


if __name__ == '__main__':
    main = Main()
    main.run()
