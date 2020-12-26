from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if (len(arr) == 0) or (len(arr) == 1 and arr[0] != elem) or (elem < arr[0]) or (elem > arr[len(arr)-1]):
        return None
    elif len(arr) == 1 and arr[0] == elem:
        return 0

    part = arr
    result = 0
    while len(part) > 2:
        ind = len(part) // 2
        val = part[ind]
        if elem < val:
            part = part[:ind]
        elif elem > val:
            part = part[ind:]
            result += ind
        else:
            part = part[:ind + 1]
        if len(part) == 2 and part[1] == elem:
            return result+1
        elif len(part) <= 2 and part[0] == elem:
            return result
        elif len(part) <= 2 and part[0] != elem:
            return None

    print(elem, arr)
    return result
