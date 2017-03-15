def gen_subsets(L):
    """Note that this fn has exponential complexity: O(2^n)."""
    res = []
    if len(L) == 0:
        return [[]]  # list of empty set
    smaller = gen_subsets(L[:-1])  # all subsets without last elements
    extra = L[-1:]  # list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one last element
    return smaller+new  # combine those with last element and those without


def count(ls):
    counter = 0
    for _ in ls:
        counter += 1
    return counter


l = [1, 2, 3, 4]
print(gen_subsets(l), count(gen_subsets(l)))
print(gen_subsets([1, 2, 2]), count(gen_subsets([1, 2, 2])))


