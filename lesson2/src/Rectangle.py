from lesson3.src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, length, width, name='Rectangle'):
        if length <= 0 or width <= 0:
            raise ValueError('Стороны должны быть больше 0')
        super().__init__(name)
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)
