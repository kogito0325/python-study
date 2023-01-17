from pygame.display import flip
from pygame.event import get as event_get

from color import Color
from display import Display
from handler import Mouse, Keyboard, Quit
from globals import Global


class Main:
    def __init__(self):
        Global.quit = Quit()
        Global.display = Display(1000, 800, '2021.08.05')
        Global.mouse = Mouse()
        Global.keyboard = Keyboard()

    @staticmethod
    def handle():
        for event in event_get():
            Global.quit.handle(event)
            Global.mouse.handle(event)
            Global.keyboard.handle(event)

    @staticmethod
    def tick():
        Global.display.tick()

        Global.mouse.clear_status()
        Global.keyboard.clear_status()

    @staticmethod
    def render():
        Global.display.window.fill(Color.WHITE)

        flip()

    def run(self):
        while Global.quit.running:
            self.handle()
            self.tick()
            self.render()


if __name__ == '__main__':
    program = Main()
    program.run()
