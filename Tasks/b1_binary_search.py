from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    half = len(arr) // 2
    left = 0
    right = len(arr) - 1
    while arr[half] != elem and left <= right:
        if elem < arr[half]:
            right = half - 1
        else:
            left = half + 1
        half = (left + right) // 2

    if left > right:
        return None
    elif arr[0] == arr[len(arr)-1]:
        return 0
    else:
        while arr[half] == arr[half - 1]:
            half -= 1
        return half
