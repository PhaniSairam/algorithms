def quick_sort(A: list) -> None:
    first = 0
    last = len(A) - 1
    my_quick_sort(A, first, last)


def my_quick_sort(A: list, first: int, last: int) -> None:
    if first < last:
        p = partition(A, first, last)
        my_quick_sort(A, first, p - 1)
        my_quick_sort(A, p + 1, last)


def partition(A: list, first: int, last: int) -> int:
    pivot_position = get_pivot(A, first, last)
    # print("Pivot Position : ", pivot_position, ": ", A[pivot_position], end=", ")
    pivot_value = A[pivot_position]
    A[pivot_position], A[first] = A[first], A[pivot_position]
    border = next = first
    while next <= last:
        if A[next] < pivot_value:
            border += 1
            A[next], A[border] = A[border], A[next]
        next += 1
    A[first], A[border] = A[border], A[first]
    # print("Border : ", border, ": ", A[border])
    return border


def get_pivot(A: list, first: int, last: int) -> int:
    mid = (first + last) // 2
    from statistics import median

    pivot = median([A[first], A[mid], A[last]])
    return A.index(pivot)


from random import sample

A = sample(range(-100, 1000), 250)

quick_sort(A)
print(A)
