from datetime import datetime
from math import cos, pi, sin

from color import RED, BLACK
from font import Font
from objects import Object, Text, Line


class Clock(Object):
    def __init__(self, x: int, y: int, font: Font, radius: int):
        super().__init__(x, y)

        self.radius = radius

        self.numbers = []
        for i in range(12):
            nx = self.x + self.radius * cos((i - 2) * pi / 6)
            ny = self.y + self.radius * sin((i - 2) * pi / 6)
            number = str(i + 1)
            text = Text(int(nx), int(ny), number, font)
            text.set_x(text.x - text.surface.get_width() / 2) \
                .set_y(text.y - text.surface.get_height() / 2)
            self.numbers.append(text)

        self.hour_hand = Line(self.x, self.y, self.x, self.y, BLACK, 10)
        self.minute_hand = Line(self.x, self.y, self.x, self.y, BLACK, 5)
        self.second_hand = Line(self.x, self.y, self.x, self.y, RED, 1)

    def tick(self):
        now = datetime.now()

        self.second_hand.set_end_pos(self.x + 1.1 * self.radius
                                     * cos((now.second - 15 + now.microsecond / 1e6) / 30 * pi),
                                     self.y + 1.1 * self.radius
                                     * sin((now.second - 15 + now.microsecond / 1e6) / 30 * pi))
        self.minute_hand.set_end_pos(self.x + self.radius * cos((now.minute - 15 + now.second / 60) / 30 * pi),
                                     self.y + self.radius * sin((now.minute - 15 + now.second / 60) / 30 * pi))
        self.hour_hand.set_end_pos(self.x + 0.75 * self.radius * cos((now.hour - 3 + now.minute / 60) / 6 * pi),
                                   self.y + 0.75 * self.radius * sin((now.hour - 3 + now.minute / 60) / 6 * pi))

    def render(self):
        for number in self.numbers:
            number.render()

        self.hour_hand.render()
        self.minute_hand.render()
        self.second_hand.render()
