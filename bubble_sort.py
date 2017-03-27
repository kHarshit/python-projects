def bubble_sort(ls):
    """The complexity of this algorithm is O(n^2)."""
    flag = False
    while not flag:
        flag = True
        for i in range(1, len(ls)):
            if ls[i-1] > ls[i]:
                temp = ls[i]
                ls[i] = ls[i-1]
                ls[i-1] = temp
                flag = False

list_in = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(list_in)
bubble_sort(list_in)
print(list_in)
