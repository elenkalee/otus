from math import sqrt
import pytest
from lesson3.src.Figure import Figure
from lesson3.src.Triangle import Triangle


class TestTriangle:
    valid_side = [[12, 13, 14], [3, 4, 5], [7, 7, 7]]
    invalid_side = [[0, -13, 14], [1, 4, 5], [7, 67, 7]]

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_create_triangle(self, valid_side):
        triangle = Triangle(*valid_side)
        assert triangle.name == 'Triangle'

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_triangle_is_figure(self, valid_side):
        triangle = Triangle(*valid_side)
        assert isinstance(triangle, Figure)

    @pytest.mark.parametrize("invalid_side", invalid_side)
    def test_invalid_sides_triangle(self, invalid_side):
        with pytest.raises(ValueError):
            Triangle(*invalid_side)

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_check_perimeter_triangle(self, valid_side):
        triangle = Triangle(*valid_side)
        assert triangle.perimeter == sum(valid_side)

    @pytest.mark.parametrize("valid_side", valid_side)
    def test_check_area_square(self, valid_side):
        triangle = Triangle(*valid_side)
        assert triangle.area == (
            sqrt(sum(valid_side) / 2 * (sum(valid_side) / 2 - valid_side[0]) * (sum(valid_side) / 2 - valid_side[1]) * (
                    sum(valid_side) / 2 - valid_side[2])))

    @pytest.mark.parametrize("valid_side_1", valid_side)
    @pytest.mark.parametrize("valid_side_2", reversed(valid_side))
    def test_add_area_square(self, valid_side_1, valid_side_2):
        triangle_1 = Triangle(*valid_side_1)
        triangle_2 = Triangle(*valid_side_2)
        area_1 = (sqrt(sum(valid_side_1) / 2 * (sum(valid_side_1) / 2 - valid_side_1[0]) * (
                sum(valid_side_1) / 2 - valid_side_1[1]) * (
                               sum(valid_side_1) / 2 - valid_side_1[2])))
        area_2 = (sqrt(sum(valid_side_2) / 2 * (sum(valid_side_2) / 2 - valid_side_2[0]) * (
                sum(valid_side_2) / 2 - valid_side_2[1]) * (
                               sum(valid_side_2) / 2 - valid_side_2[2])))
        assert triangle_1.add_area(triangle_2) == area_1 + area_2
