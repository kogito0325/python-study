from color import WHITE
from globals import Global
from objects import Line


class RainDrop(Line):
    COLOR = WHITE

    def __init__(self, x: int, length: int):
        super().__init__(x=x, y=-length, x2=x, y2=0, color=RainDrop.COLOR, width=length // 30)

        self.speed = length * 20

    def tick(self):
        offset = self.speed / Global.display.fps
        self.y += offset
        self.y2 += offset

        if self.y >= Global.display.height:
            Global.object_manager.remove(self)
