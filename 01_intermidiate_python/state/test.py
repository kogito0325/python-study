from color import WHITE, ORANGE
from font import Font
from globals import Global
from objects import Text, FireworkBody
from objects.button import TextButton
from state import State


class Test1(State):
    def __init__(self):
        super().__init__()

        font = Font('res/font/Pretendard-Bold.otf', 42, WHITE)

        self.object_manager\
            .add(Text(200, 300, '이것은 Test1입니다', font))\
            .add(TextButton(200, 600, 300, 100, ORANGE,
                            lambda: Global.state_manager.set_state(Test2()), 'Text2 가기', font))


class Test2(State):
    def __init__(self):
        super().__init__()

        font = Font('res/font/Pretendard-Bold.otf', 42, WHITE)

        self.object_manager\
            .add(TextButton(600, 600, 300, 100, ORANGE,
                            lambda: Global.state_manager.set_state(Test1()), '돌아가기', font))

    def tick(self):
        super().tick()

        if Global.mouse.left_start:
            self.object_manager.add(FireworkBody(Global.mouse.x, Global.mouse.y, self.object_manager))
