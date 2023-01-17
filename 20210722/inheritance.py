from practice import calculator


class ComplexCalculator(calculator.Calculator):
    def __init__(self, default_value: float = 0):
        super().__init__(default_value)

    def add(self, *xs: float):
        for x in xs:
            self.value += x

    def pow(self, x: float):
        self.value **= x


complex_calculator = ComplexCalculator()
complex_calculator.add(12, 24)
complex_calculator.pow(2)

print(complex_calculator.value)
