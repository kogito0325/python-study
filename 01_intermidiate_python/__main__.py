from datetime import datetime

from pygame import init
from pygame.display import flip
from pygame.event import get as event_get

from color import NIGHT_SKY
from display import Display
from globals import Global
from handler import Mouse, Keyboard, QuitHandler
from manager import ObjectManager, StateManager
from state import Test1, Assignment1

init()


class Main:
    def __init__(self):
        self.running = True
        self.quit_handler = QuitHandler(self.shutdown)

        now = datetime.now()

        Global.display = Display(500, 400, f'{now.year}. {now.month}. {now.day} Basic Python I')
        Global.mouse = Mouse()
        Global.keyboard = Keyboard()

        Global.object_manager = ObjectManager()
        Global.state_manager = StateManager().set_state(Assignment1())

        # font = Font('res/font/Pretendard-Bold.otf', 100, BLACK)
        # Global.object_manager.add(TextButton(100, 100, 300, 100, WHITE, lambda: Global.object_manager.add(
        #     FireworkBody(randint(0, Global.display.width), Global.display.height)), '발사!', font))

    def shutdown(self):
        self.running = False

    def handle(self):
        for event in event_get():
            self.quit_handler.handle(event)
            Global.display.handle(event)
            Global.mouse.handle(event)
            Global.keyboard.handle(event)

    @staticmethod
    def tick():
        Global.display.tick()

        # probability = 1 / Global.display.fps
        # if random() < probability:
        #     Global.object_manager.add(FireworkBody(random() * Global.display.width, Global.display.height))
        # if Global.mouse.left_start:
        #     Global.object_manager.add(FireworkBody(Global.mouse.x, Global.mouse.y))

        Global.state_manager.tick()
        Global.object_manager.tick()

        Global.mouse.clear_status()
        Global.keyboard.clear_status()

    @staticmethod
    def render():
        Global.display.window.fill(NIGHT_SKY)

        Global.state_manager.render()
        Global.object_manager.render()

        flip()

    def run(self):
        while self.running:
            self.handle()
            self.tick()
            self.render()


if __name__ == '__main__':
    program = Main()
    program.run()
