import timeit

setup = """import random
import Tasks.g0_bubble_sort as bubble
import Tasks.g1_merge_sort as merge
import Tasks.g2_quick_sort as quick
import sys"""


code_bubble = """
arr = [random.randint(13, 25) for number in range(4*(10**3))]
bubble.sort(arr)"""


code_merge = """
arr = [random.randint(13, 25) for number in range(10**5)]
merge.sort(arr)"""


code_quick = """
arr = [random.randint(13, 25) for number in range(10**4)]
quick.sort(arr)"""


print("Setup is:\n", setup)
number = 1

print(code_bubble)
print(code_merge)
print(code_quick, "\n")

taken_time = timeit.timeit(stmt=code_bubble, setup=setup, number=number)
print("Bubble sort takes", taken_time, "seconds")
taken_time = timeit.timeit(stmt=code_merge, setup=setup, number=number)
print("Merge sort takes", taken_time, "seconds")
taken_time = timeit.timeit(stmt=code_quick, setup=setup, number=number)
print("Quick sort takes", taken_time, "seconds")

