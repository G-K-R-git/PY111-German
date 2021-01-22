from typing import List
import random
import time


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container
    else:
        sorted_container = []
        # Разделение на две половинки
        middle = len(container) // 2
        left = container[0:middle]
        right = container[middle:len(container)]
        # Рекурсивный вызов функции до момента, пока не останется 1 элемент
        left_sorted = sort(left)
        right_sorted = sort(right)
        # Сортировка половинок
        i, j = 0, 0
        while True:
            if left_sorted[i] <= right_sorted[j]:
                sorted_container.append(left_sorted[i])
                i += 1
            else:
                sorted_container.append(right_sorted[j])
                j += 1
            if i == len(left_sorted):  # Вставка конца оставшейся половинки в отсортированный массив
                sorted_container.extend(right_sorted[j:])
                return sorted_container
            elif j == len(right_sorted):
                sorted_container.extend(left_sorted[i:])
                return sorted_container


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(2000001)]  # 9 s with slices|
    start = time.time()
    arr2 = sort(arr)
    print(time.time() - start)
    print(arr2 == sorted(arr))
