from lesson3.src.Figure import Figure


class Square(Figure):

    def __init__(self, side, name='Square'):
        if side <= 0:
            raise ValueError('Сторона должна быть больше 0')
        super().__init__(name)
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4
