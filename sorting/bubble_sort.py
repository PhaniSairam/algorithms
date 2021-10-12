def bubble_sort(A: list) -> list:
    for i in range(1, len(A)):
        print("iteration - ", i, " --> ", A)
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


A = [9, 8, 7, 6, 5, 4, 3, 1, 2]
bubble_sort(A)
