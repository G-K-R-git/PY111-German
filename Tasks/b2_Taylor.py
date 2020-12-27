"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    precision = 10
    sum = 1
    fuct = 1
    y = x
    for i in range(1, precision):
        sum += y/fuct
        y = y*x
        fuct *=(i+1)
    return sum


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    precision = 5
    y = x
    sum = y
    fuct = 1
    sign = 1
    for i in range(3,precision*2, 2):
        sign *= -1
        y = y*x*x
        fuct *= i*(i-1)
        sum += sign*y/fuct
    return sum
