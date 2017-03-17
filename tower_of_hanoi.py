# The objective is to transfer the entire tower to one of the other pegs, moving
# only one disk at a time and never moving a larger one onto a smaller.


def hanoi_tower(n, source, helper, target):
    if n == 1:
        print('move from ' + str(source) + ' to ' + str(target))
    else:
        hanoi_tower(n - 1, source, target, helper)
        hanoi_tower(1, source, helper, target)
        hanoi_tower(n - 1, helper, source, target)

print(hanoi_tower(3, 'P1', 'P2', 'P3'))


def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n-1, source, target, helper)
        if source:  # if there is an element in source
            target.append(source.pop())
        hanoi(n-1, helper, source, target)

s = [5, 4, 3, 2, 1]
h = []
t = []

hanoi(len(s), s, h, t)
print(s, h, t)


def hanoi_steps(n, source, helper, target):
    """provides a step by step guide"""
    # print("hanoi(", source, helper, target, "called")
    if n > 0:
        hanoi_steps(n - 1, source, target, helper)
        if source[0]:
            disk = source[0].pop()
            print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)
        hanoi_steps(n - 1, helper, source, target)

source_p = ([4, 3, 2, 1], "T1")
helper_p = ([], "T2")
target_p = ([], "T3")
hanoi_steps(len(source_p[0]), source_p, helper_p, target_p)
