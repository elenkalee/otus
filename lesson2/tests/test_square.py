from lesson3.src.Figure import Figure
from lesson3.src.Square import Square
import pytest


class TestSquare:
    valid_side = [1, 7.9, 56]
    invalid_side = [-1, 0, -7.9]

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_create_square(self, valid_side):
        square = Square(valid_side)
        assert square.name == 'Square'

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_square_is_figure(self, valid_side):
        square = Square(valid_side)
        assert isinstance(square, Figure)

    @pytest.mark.parametrize("invalid_side", invalid_side)
    def test_sides_less_than_0_square(self, invalid_side):
        with pytest.raises(ValueError):
            Square(invalid_side)

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_check_perimetr_square(self, valid_side):
        square = Square(valid_side)
        assert square.perimeter == valid_side * 4

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_check_area_square(self, valid_side):
        square = Square(valid_side)
        assert square.area == valid_side ** 2

    @pytest.mark.parametrize("valid_side_1", valid_side)
    @pytest.mark.parametrize("valid_side_2", reversed(valid_side))
    def test_add_area_square(self, valid_side_1, valid_side_2):
        square_1 = Square(valid_side_1)
        square_2 = Square(valid_side_2)
        assert square_1.add_area(square_2) == valid_side_1 ** 2 + valid_side_2 ** 2
