"""
Time complexity - O(n2)/O(n square)
Compares the element with previous element and swaps the current element with previous one
Not so fast sort, better for smaller datasets, expect better performance up until 10,000 elements
"""
def insertion_sort_with_swap(A: list) -> list:
    # print("List - ", A)
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
            else:
                break
    return A


def insertion_sort(A: list) -> list:
    # print("List - ", A)
    for i in range(1, len(A)):
        curNum = A[i]
        j = i
        while j > 0 and A[j - 1] > curNum:
            A[j] = A[j - 1]
            j -= 1
        A[j] = curNum
    return A


A = [14, 9, 33, 27, 10, 35, 19, 42, 44]
from copy import deepcopy
from random import sample
import time

A = sample(range(-100, 300), 250)
B = deepcopy(A)
tic = time.perf_counter()
print(insertion_sort_with_swap(A))
toc = time.perf_counter()
print(f"Insertion Sort with swap, ran for -  {toc - tic:0.4f} seconds")
tic = time.perf_counter()
print(insertion_sort(B))
toc = time.perf_counter()
print(f"Insertion Sort without swap, ran for -  {toc - tic:0.4f} seconds")
