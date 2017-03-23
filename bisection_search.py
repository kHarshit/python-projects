"""The list must already be sorted in order for bisection search to work."""


def bisect_search(l, e):
    low = 0
    high = len(l)-1
    found = False
    while low <= high and not found:
        mid = (low+high)//2
        if l[mid] == e:
            found = True
        elif l[mid] < e:
            low = mid + 1
        elif l[mid] > e:
            high = mid - 1
    return found


def bisection_search(l, e):
    """recursive algorithm"""
    if l == []:
        return False
    elif len(l) == 1:
        return l[0] == e
    else:
        mid = len(l)//2
        if l[mid] > e:
            return bisection_search(l[:mid], e)
        else:
            return bisection_search(l[mid:], e)

print(bisect_search([1, 2, 3, 4, 5], 3))
print(bisection_search([1, 2, 3, 4, 5], 3))
