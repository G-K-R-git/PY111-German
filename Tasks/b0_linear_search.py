"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_val = arr[0]
    ind = 0
    count = 0
    for i in arr:
        if min_val > i:
            min_val = i
            ind = count
        count += 1
    print(arr)
    return ind
