from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    suffix = 0
    for i in range(len(container)-1-suffix):
        for j in range(len(container)-1-suffix):
            if container[j] > container[j+1]:
                container[j], container[j+1] = container[j+1], container[j]
        suffix += 1
    return container


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(30)]
    print(arr)
    print(sort(arr))