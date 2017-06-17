"""pseudo-code"""

"""
BUBBLE-SORT(A):  // A[1....A.length]
for i=1 to A.length - 1
    for j=A.length downto i + 1
        if A[j] < A[j-1]
            exchange A[j] with A[j-1]
"""


# def bubble_sort(ls):
#     """The complexity of this algorithm is O(n^2)."""
#     flag = False
#     while not flag:
#         flag = True
#         for i in range(1, len(ls)):
#             if ls[i-1] > ls[i]:
#                 ls[i], ls[i-1] = ls[i-1], ls[i]
#                 flag = False

def bubble_sort(ls):
    """The complexity of this algorithm is O(n^2)."""
    for i in range(len(ls)-2):
        for j in range(len(ls)-1, i, -1):
            if ls[j-1] > ls[j]:
                ls[j], ls[j-1] = ls[j-1], ls[j]


list_in = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(list_in)
bubble_sort(list_in)
print(list_in)
