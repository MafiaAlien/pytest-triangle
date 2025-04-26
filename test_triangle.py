# assert if it is a triangle
# assert if it is an Equilateral triangle
# assert if it is an isosceles triangle
# assert if one of its edge is less than 1, or negtive 
from triangle import Triangle
import pytest

@pytest.mark.parametrize(
    "sides, expected",
    [
        ((3, 4, 5), True),     
        ((5, 5, 5), True),    
        ((5, 12, 13), True),  
        ((7, 10, 5), True),  
        ((2, 2, 3), True),   
        ((1, 1, 2), False),    
        ((1, 2, 3), False), 
        ((10, 1, 1), False),  
        ((0, 0, 0), False),    
        ((1000, 1, 1), False), 
    ]
)
def test_triangle_validity(sides, expected):
    t = Triangle(*sides)
    assert t.is_valid() == expected
