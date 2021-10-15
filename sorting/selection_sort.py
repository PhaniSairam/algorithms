"""
Time Complexity : O(n square)/O(n**2)
Not so fasting sorting algorithm, because it uses nested loops.
Useful only for really smaller datasets, at max upto 10,000 elements.
"""
from typing import List


def selection_sort(my_list: List) -> List:
    for i in range(len(my_list) - 1):
        min_pos = i
        print("iteration - ", i, " --> ", my_list)
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_pos]:
                min_pos = j
        if min_pos != i:
            my_list[i], my_list[min_pos] = my_list[min_pos], my_list[i]
    return my_list


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# A = sample(range(-100, 1000), 250)
print(selection_sort(A))
