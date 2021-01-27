from typing import List
import random


def separate(container, first, last):
    """
    Function to identify start-stop index for next recursive sorting

    :param container: input array
    :param first: first index from which to sort
    :param last: last index till which to sort
    :return: border index for next sorting
    """
    i = first
    j = last
    base = (container[last] + container[first]) // 2
    while i < j:
        while container[i] <= base and i < j:
            i += 1
        while container[j] > base and i < j:
            j -= 1
        if i < j:
            container[i], container[j] = container[j], container[i]
    return i


def quick_sort(container: List[int], first, last) -> List[int]:
    """
    Sort input container in range index from first to last

    :param container: input array
    :param first: first index from which to sort
    :param last: last index till which to sort
    :return: input array if it has length of 1 or 2
    """
    if len(container) == 1:
        return container
    if len(container) == 2:
        if container[0] <= container[1]:
            return container
        else:
            container[1], container[0] = container[0], container[1]
            return container
    if first == last-1:
        if container[first] > container[last]:
            container[first], container[last] = container[last], container[first]
    elif first < last:
        border = separate(container, first, last)
        quick_sort(container, first, border - 1)
        quick_sort(container, border, last)


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    container_length = len(container)
    quick_sort(container, 0, container_length - 1)
    return container


# def sort2(container: List[int]) -> List[int]:
    # Variant with SLICES
    # if len(container) == 1:
    #     return container
    # if len(container) == 2:
    #     if container[0] <= container[1]:
    #         return container
    #     else:
    #         container[1], container[0] = container[0], container[1]
    #         return container
    # base_value = (container[0]+container[len(container)//2]+container[-1])//3
    # i = 0
    # j = len(container)-1
    # while i < j:
    #     while container[i] <= base_value and i <= j:
    #         i += 1
    #     while container[j] >= base_value and j >= i:
    #         j -= 1
    #     if j >= i:
    #         container[i], container[j] = container[j], container[i]
    # left = sort(container[0:i])
    # right = sort(container[i:])
    # result = left + right
    # return result


if __name__ == '__main__':
    for i in range(10000):
        arr = [random.randint(-100, 100) for _ in range(100)]
        print("Initial array: \n", arr)
        sorteed = sort(arr)
        print("Sorted", sorteed)
    arr = [0 for i in range(100)]
    # arr = [-2, 1, -1, -5, -5]
    print("Initial array: \n", arr)
    sorteed = sort(arr)
    print("Sorted", sorteed)
