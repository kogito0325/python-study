class Object:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def set_x(self, x: int) -> 'Object':
        self.x = x
        return self

    def set_y(self, y: int) -> 'Object':
        self.y = y
        return self

    def tick(self):
        pass

    def render(self):
        pass
