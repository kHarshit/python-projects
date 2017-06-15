"""pseudo code"""

"""
PARTITION(A, l, r):
p = A[l]
i = l + 1
for j=l+1 to r
    if A[j] < p  // if A[j] > p, do nothing
        swap A[j] and A[i]
        i = i + 1
swap A[l] and A[i-1]
return

QUICKSORT(A, l, r):
if l < r
    p = PARTITION(A, l, r)
    QUICKSORT(A, l, p-1)
    QUICKSORT(A, p+1, r)

"""


def partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(i, r):
        if A[j] <= p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i


def qsort(A, l, r):
    """uses quick-sort to return a sorted array"""
    if l < r:
        q = partition(A, l, r)
        qsort(A, l, q-1)
        qsort(A, q+1, r)


def sort(A):
    qsort(A, 0, len(A)-1)

list_in = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(list_in)
sort(list_in)
print(list_in)