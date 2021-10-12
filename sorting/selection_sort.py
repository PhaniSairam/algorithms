def selection_sort(A: list) -> list:
    for i in range(len(A) - 1):
        minPos = i
        print("iteration - ", i, " --> ", A)
        for j in range(i + 1, len(A)):
            if A[j] < A[minPos]:
                minPos = j
        if minPos != i:
            A[i], A[minPos] = A[minPos], A[i]
    return A


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# A = sample(range(-100, 1000), 250)
print(selection_sort(A))
