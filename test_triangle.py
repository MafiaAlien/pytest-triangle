# assert if it is a triangle
# assert if it is an Equilateral triangle
# assert if it is an isosceles triangle
# assert if one of its edge is less than 1, or negtive 
from triangle import Triangle
import pytest

@pytest.mark.parametrize(
    "sides, expected",
    [
        ((3, 4, 5), True),     # 合法三角形
        ((5, 5, 5), True),     # 等边三角形
        ((5, 12, 13), True),   # 勾股三角形
        ((7, 10, 5), True),    # 普通三角形
        ((2, 2, 3), True),     # 等腰三角形
        ((1, 1, 2), False),    # 两边之和 = 第三边 ❌
        ((1, 2, 3), False),    # 两边之和 < 第三边 ❌
        ((10, 1, 1), False),   # 明显不合法 ❌
        ((0, 0, 0), False),    # 边长为0 ❌
        ((1000, 1, 1), False), # 极端不合法 ❌
    ]
)
def test_triangle_validity(sides, expected):
    t = Triangle(*sides)
    assert t.is_valid() == expected
