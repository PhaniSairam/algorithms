"""
Time Complexity - O(n log n), worst case - O(n square)
Performance depends on selecting the right pivot.
quickSort is recursive function, Divide and Conquer algorith, very Efficient for large datasets
keywords - pivot, border, partition, median
"""
from typing import List


def quick_sort(my_list: List) -> None:
    first = 0
    last = len(my_list) - 1
    my_quick_sort(my_list, first, last)


def my_quick_sort(my_list: List, first: int, last: int) -> None:
    if first < last:
        p = partition(my_list, first, last)
        my_quick_sort(my_list, first, p - 1)
        my_quick_sort(my_list, p + 1, last)


def partition(my_list: List, first: int, last: int) -> int:
    pivot_index= get_pivot(my_list, first, last)
    # print("Pivot Position : ", pivot_index, ": ", A[pivot_index], end=", ")
    pivot_value = my_list[pivot_index]
    my_list[pivot_index], my_list[first] = my_list[first], my_list[pivot_index]
    border = next = first
    while next <= last:
        if my_list[next] < pivot_value:
            border += 1
            my_list[next], my_list[border] = my_list[border], my_list[next]
        next += 1
    my_list[first], my_list[border] = my_list[border], my_list[first]
    # print("Border : ", border, ": ", A[border])
    return border


def get_pivot(my_list: List, first: int, last: int) -> int:
    mid = (first + last) // 2
    from statistics import median

    pivot = median([my_list[first], my_list[mid], my_list[last]])
    return my_list.index(pivot)


from random import sample

A = sample(range(-100, 1000), 250)

quick_sort(A)
print(A)
