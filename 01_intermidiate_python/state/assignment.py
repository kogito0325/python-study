from pygame.constants import K_s

from color import WHITE
from font import Font
from globals import Global
from objects import AdvancedPlayer, Portal, Text
from state import State


class Assignment1(State):
    def __init__(self):
        super().__init__()

        self.font = Font('res/font/Pretendard-Bold.otf', 42, WHITE)

        self.player = AdvancedPlayer()
        self.portal = Portal()
        self.object_manager.add(self.portal).add(Text(200, 300, 'State - 1', self.font)).add(self.player)

    def tick(self):
        super().tick()

        if Global.keyboard.is_start(K_s) and self.player.x > self.portal.x \
                and self.player.x + self.player.width < self.portal.x + self.portal.width \
                and self.player.y > self.portal.y \
                and self.player.y + self.player.height < self.portal.y + self.portal.height:
            print("portal1 used")
            Global.state_manager.set_state(Assignment2())


class Assignment2(State):
    def __init__(self):
        super().__init__()

        self.font = Font('res/font/Pretendard-Bold.otf', 42, WHITE)

        self.player = AdvancedPlayer()
        self.portal = Portal()
        self.object_manager.add(self.portal).add(Text(200, 300, 'State - 2', self.font)).add(self.player)

    def tick(self):
        super().tick()

        if Global.keyboard.is_start(K_s) and self.player.x > self.portal.x \
                and self.player.x + self.player.width < self.portal.x + self.portal.width \
                and self.player.y > self.portal.y \
                and self.player.y + self.player.height < self.portal.y + self.portal.height:
            print("portal2 used")
            Global.state_manager.set_state(Assignment1())
