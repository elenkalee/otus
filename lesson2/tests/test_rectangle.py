from lesson3.src.Figure import Figure
import pytest
from lesson3.src.Rectangle import Rectangle


class TestRectangle:
    valid_side = [1, 7.9, 56]
    invalid_side = [-1, 0, -7.9]

    @pytest.mark.parametrize("valid_length", valid_side)
    @pytest.mark.parametrize("valid_width", reversed(valid_side))
    def test_create_rectangle(self, valid_length, valid_width):
        rectangle = Rectangle(valid_length, valid_width)
        assert rectangle.name == 'Rectangle'

    @pytest.mark.parametrize("valid_length", valid_side)
    @pytest.mark.parametrize("valid_width", reversed(valid_side))
    def test_rectangle_is_figure(self, valid_length, valid_width):
        rectangle = Rectangle(valid_length, valid_width)
        assert isinstance(rectangle, Figure)

    @pytest.mark.parametrize("invalid_length", invalid_side)
    @pytest.mark.parametrize("invalid_width", reversed(invalid_side))
    def test_sides_less_than_0_rectangle(self, invalid_length, invalid_width):
        with pytest.raises(ValueError):
            Rectangle(invalid_length, invalid_width)

    @pytest.mark.parametrize("valid_length", valid_side)
    @pytest.mark.parametrize("valid_width", reversed(valid_side))
    def test_check_perimeter_rectangle(self, valid_length, valid_width):
        rectangle = Rectangle(valid_length, valid_width)
        assert rectangle.perimeter == 2 * (valid_length + valid_width)

    @pytest.mark.parametrize("valid_length", valid_side)
    @pytest.mark.parametrize("valid_width", reversed(valid_side))
    def test_check_area_rectangle(self, valid_length, valid_width):
        rectangle = Rectangle(valid_length, valid_width)
        assert rectangle.area == valid_length * valid_width

    @pytest.mark.parametrize("valid_length", valid_side)
    @pytest.mark.parametrize("valid_width", reversed(valid_side))
    def test_add_area_rectangle(self, valid_length, valid_width):
        rectangle_1 = Rectangle(valid_length, valid_width)
        rectangle_2 = Rectangle(valid_length, valid_width)
        assert rectangle_1.add_area(rectangle_2) == 2 * valid_length * valid_width
