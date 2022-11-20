class Figure:

    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        return 0

    @property
    def perimeter(self):
        return 0

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise ValueError
