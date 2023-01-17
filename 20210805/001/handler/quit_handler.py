from pygame.constants import QUIT

from handler import Handler


class Quit(Handler):
    def __init__(self):
        self.running = True

    def handle(self, event):
        if event.type == QUIT:
            self.running = False
