import pytest
from src import calculator

@pytest.mark.parametrize("x,y,expected", [
    (2,3,5),      # both positive → add
    (-2,-3,6),    # both negative → multiply
    (5,-2,7)      # mixed signs → subtract
])
def test_smart_calculator(x, y, expected):
    assert calculator.smart_calculator(x, y) == expected
