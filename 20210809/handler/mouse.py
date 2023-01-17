from pygame.constants import MOUSEBUTTONDOWN, BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT, MOUSEBUTTONUP

from handler import Handler


class Mouse(Handler):
    def __init__(self):
        self.left = False
        self.middle = False
        self.right = False

        self.left_start = False
        self.middle_start = False
        self.right_start = False

        self.left_end = False
        self.middle_end = False
        self.right_end = False

    def handle(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == BUTTON_LEFT:
                self.left = True
                self.left_start = True
            elif event.button == BUTTON_MIDDLE:
                self.middle = True
                self.middle_start = True
            elif event.button == BUTTON_RIGHT:
                self.right = True
                self.right_start = True
        if event.type == MOUSEBUTTONUP:
            if event.button == BUTTON_LEFT:
                self.left = False
                self.left_end = True
            elif event.button == BUTTON_MIDDLE:
                self.middle = False
                self.middle_end = True
            elif event.button == BUTTON_RIGHT:
                self.right = False
                self.right_end = True

    def clear_status(self):
        self.left_start = False
        self.middle_start = False
        self.right_start = False

        self.left_end = False
        self.middle_end = False
        self.right_end = False
