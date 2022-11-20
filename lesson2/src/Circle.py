import math
from lesson3.src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name='Circle'):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        super().__init__(name)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
