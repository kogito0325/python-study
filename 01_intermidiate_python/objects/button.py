from font import Font
from globals import Global
from objects import Rectangle, Text
from util import center


class Button(Rectangle):
    def __init__(self, x: int, y: int, w: int, h: int, color: tuple, function):
        """
        클릭을 감지하고, 일정한 함수를 실행하는 오브젝트

        :param x:
        :param y:
        :param w:
        :param h:
        :param color:
        :param function:
        """
        super().__init__(x, y, w, h, color)

        self.function = function

    def tick(self):
        if Global.mouse.left_end:
            if self.x < Global.mouse.x < self.x + self.width and self.y < Global.mouse.y < self.y + self.height:
                self.function()


class TextButton(Button):
    def __init__(self, x: int, y: int, w: int, h: int, color: tuple, function, text: str, font: Font):
        """
        Button 위에다가 텍스트가 뜨면 좋겠다.

        :param x:
        :param y:
        :param w:
        :param h:
        :param color:
        :param function:
        :param text:
        :param font:
        """
        super().__init__(x, y, w, h, color, function)

        self.text_object = Text(0, 0, text, font)
        self.text_object.set_x(int(self.x + center(self.width, self.text_object.surface.get_width())))
        self.text_object.set_y(int(self.y + center(self.height, self.text_object.surface.get_height())))

    def render(self):
        super().render()
        self.text_object.render()

