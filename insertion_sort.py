"""pseudo code"""

"""
INSERTION-SORT(A):
for j=2 to A.length
    key = A[j]
    // Insert A[j] into the sorted sequence A[1..j-1]
    i = j - 1
    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
"""


def insertion_sort(A):
    """uses insertion sort to sort an array"""
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

list_in = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(list_in)
insertion_sort(list_in)
print(list_in)

