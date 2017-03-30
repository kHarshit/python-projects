def merge_sort(ls):
    """The complexity of this algorithm is O(n*log(n))"""
    if len(ls) < 2:
        return ls[:]
    else:
        mid = len(ls)//2
        left = merge_sort(ls[:mid])
        right = merge_sort(ls[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_in = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(list_in)
print(merge_sort(list_in))
