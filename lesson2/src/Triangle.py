from math import sqrt
from lesson3.src.Figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c, name='Triangle'):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Стороны должны быть больше 0')
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError('Такого треугольника не существует')
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return (sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (
                half_perimeter - self.c)))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
