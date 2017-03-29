def selection_sort(ls):
    """The complexity of this algorithm is O(n^2)."""
    min = 0
    while min != len(ls):
        for i in range(min, len(ls)):
            if ls[i] < ls[min]:
                ls[min], ls[i] = ls[i], ls[min]
        min += 1

list_in = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(list_in)
selection_sort(list_in)
print(list_in)
