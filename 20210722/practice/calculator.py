class Calculator:
    def __init__(self, default_value):
        self.value = default_value

    def add(self, x: float):
        self.value += x

    def sub(self, x: float):
        self.value -= x

    def mul(self, x: float):
        self.value *= x

    def div(self, x: float):
        self.value /= x
