"""
Time Complexity - O(n log n)
MergeSort is recursive, Divide and Conquer algorithm and Very efficient for large data sets,not so efficient for smaller datasets.
Splits the list down to half, up until it becomes a list of single element and merges them back in sorting order
"""
from typing import List


def merge_sort(my_list: List) -> None:
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]
        print(f"merge_soft(left) - {left}")
        print(f"merge_soft(right) - {right}")
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            # print(i, left[i], right[i])
            if left[i] <= right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


A = [14, 9, 33, 27, 10, 35, 19, 42, 44]
print(f"merge_sort(A) - {A}")
merge_sort(A)
print(A)
