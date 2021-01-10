from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :param accumulator: accumulator for needed index
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if len(arr) == 0:
        return None
    if arr[0] == arr[-1]:
        return 0


    def binary_search2(elem: int, arr: Sequence, accumulator: int = 0) -> Optional[int]:
        if len(arr) == 0:
            return None
        else:
            half = len(arr) // 2
            index = half
            accumulator += index
            # print('current array is: ', arr, index, '|', accumulator)
            if arr[index] == elem:
                return accumulator
            elif arr[index] >= elem:
                return binary_search2(elem, arr[:index], accumulator-index)
            elif arr[index] <= elem:
                return binary_search2(elem, arr[index+1:], accumulator+1)

    searched_elem_index = binary_search2(elem, arr)
    if searched_elem_index is not None:
        while arr[searched_elem_index] == arr[searched_elem_index-1]:
            searched_elem_index -= 1
        return searched_elem_index
    else:
        return None
