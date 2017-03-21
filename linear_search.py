def linear_search(L, e):
    """The complexity of this algorithm is O(n) where n is len(L)"""
    found = False
    for i in range(len(L)):
        if L[i] == e:
            found = True
    return found


def search_sorted(L, e):
    """linear search on sorted list.
    The complexity of this algorithm is also O(n) where n is len(L)"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

ls = [1, 4, 3, 2]
ls_sorted = [1, 2, 3, 4]
n = 3

print(linear_search(ls, n))
print(search_sorted(ls_sorted, n))
