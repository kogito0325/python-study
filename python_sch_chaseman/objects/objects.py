# objects

class Object:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self

    def tick(self):
        pass

    def render(self):
        pass

