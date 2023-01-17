from pygame.constants import KEYDOWN, KEYUP

from handler import Handler


class Keyboard(Handler):
    def __init__(self):
        self.keys = set()
        self.start = set()
        self.end = set()

    def handle(self, event):
        if event.type == KEYDOWN:
            self.keys.add(event.key)
            self.start.add(event.key)
        elif event.type == KEYUP:
            self.keys.remove(event.key)
            self.end.add(event.key)

    def clear_status(self):
        self.start.clear()
        self.end.clear()

    def is_pressed(self, key):
        return key in self.keys

    def is_start(self, key):
        return key in self.start

    def is_end(self, key):
        return key in self.end
