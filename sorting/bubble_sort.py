"""
Time Complexity - O(n)
Not so fast algorithm, for larger datasets recommended to go for merge/quick sort.
"""
from typing import List


def bubble_sort(my_list: List) -> List:
    for i in range(1, len(my_list)):
        print("iteration - ", i, " --> ", my_list)
        for j in range(0, len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


A = [9, 8, 7, 6, 5, 4, 3, 1, 2]
bubble_sort(A)
