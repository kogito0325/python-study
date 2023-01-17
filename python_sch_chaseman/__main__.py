from pygame import init
from pygame.display import flip
from pygame.event import get as event_get

from color import Color
from display import Display
from globals import Global
from handler import Mouse, Keyboard, Quit
from objects import Player, Enemy

init()


class Main:
    def __init__(self):
        Global.quit = Quit()
        Global.display = Display(1000, 800, '2021.08.05')
        Global.mouse = Mouse()
        Global.keyboard = Keyboard()

        self.player = Player(100, 100)
        self.enemy = Enemy(800, 500, self.player)

    @staticmethod
    def handle():
        for event in event_get():
            Global.quit.handle(event)
            Global.mouse.handle(event)
            Global.keyboard.handle(event)

    def tick(self):
        Global.display.tick()

        self.player.tick()
        self.enemy.tick()

        Global.mouse.clear_status()
        Global.keyboard.clear_status()

    def render(self):
        Global.display.window.fill(Color.WHITE)

        self.player.render()
        self.enemy.render()

        flip()

    def run(self):
        while Global.quit.running:
            self.handle()
            self.tick()
            self.render()


if __name__ == '__main__':
    program = Main()
    program.run()
