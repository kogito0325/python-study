from pygame.constants import QUIT, K_ESCAPE

from globals import Global
from handler import Handler


class QuitHandler(Handler):
    def __init__(self, shutdown):
        self.shutdown = shutdown

    def handle(self, event):
        if event.type == QUIT or Global.keyboard.is_pressed(K_ESCAPE):
            self.shutdown()
