import math
import pytest

from lesson3.src.Figure import Figure
from lesson3.src.Circle import Circle


class TestCircle:

    valid_radius = [1, 5, 9.8]
    invalid_radius = [0, -5, -9.8]

    @pytest.mark.parametrize("valid_radius", valid_radius)
    def test_create_circle(self, valid_radius):
        circle = Circle(valid_radius)
        assert circle.name == 'Circle'

    @pytest.mark.parametrize("valid_radius", valid_radius)
    def test_circle_is_figure(self, valid_radius):
        circle = Circle(valid_radius)
        assert isinstance(circle, Figure)

    @pytest.mark.parametrize("invalid_radius", invalid_radius)
    def test_radius_less_than_0_circle(self, invalid_radius):
        with pytest.raises(ValueError):
            Circle(invalid_radius)

    @pytest.mark.parametrize("valid_radius", valid_radius)
    def test_check_perimeter_circle(self, valid_radius):
        circle = Circle(valid_radius)
        assert circle.perimeter == 2 * math.pi*valid_radius

    @pytest.mark.parametrize("valid_radius", valid_radius)
    def test_check_area_circle(self, valid_radius):
        circle = Circle(valid_radius)
        assert circle.area == math.pi * valid_radius ** 2

    @pytest.mark.parametrize("valid_radius_1", valid_radius)
    @pytest.mark.parametrize("valid_radius_2", reversed(valid_radius))
    def test_add_area_circle(self, valid_radius_1, valid_radius_2):
        circle_1 = Circle(valid_radius_1)
        circle_2 = Circle(valid_radius_2)
        assert circle_1.add_area(circle_2) == (math.pi * valid_radius_1 ** 2) + (math.pi * valid_radius_2 ** 2)
