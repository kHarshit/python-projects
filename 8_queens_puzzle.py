# As told by Wikipedia, “The eight queens puzzle is the problem of placing eight chess queens
# on an 8x8 chessboard so that no two queens attack each other. Thus, a solution requires that
# no two queens share the same row, column, or diagonal.”

# One of the solutions of our problems is:
# bd = [(0,6), (1,4), (2,2), (3,0), (4,5), (5,7), (6,1), (7,3)]
# The first coordinates are 0,1,2,3,4,5,6,7 and they correspond exactly to the index position of the pairs in the list.
# So, we can ignore them to come up with compact solution: bd = [6, 4, 2, 0, 5, 7, 1, 3]

# In our representation, any solution to the N queens problem must therefore be a
# permutation of the numbers [0 .. N-1].

# If we only use permutations of the rows, and we’re using our compact representation, no queens can clash on
# either rows or columns, and we don’t even have to concern ourselves with those cases. So the only clashes we
# need to test for are clashes on the diagonals.


def share_dia(x0, y0, x1, y1):
    """Is (x0, y0) on a shared diagonal as (x1, y1)?"""
    dy = y1 - y0
    dx = x1 - x0
    return dy == dx

# So the next building block is a function that, given a partially completed puzzle, can check
# whether the queen at column c clashes with any of the queens to its left, at columns 0,1,2,..c-1:


def col_clashes(bs, c):
    """Checks if queen at column c clashes with any queen to its left."""
    for i in range(c):
        if share_dia(i, bs[i], c, bs[c]):
            return True
    return False  # no clashes; column c has a safe placement

# Finally, we’re going to give our program one of our permutations — i.e. all queens placed somewhere,
# one on each row, one on each column. But does the permutation have any diagonal clashes?


def has_clashes(the_board):
    """Determine whether we have any queens clashing on the diagonals.
        We’re assuming here that the_board is a permutation of column
        numbers, so we’re not explicitly checking row or column clashes."""
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

# Now, We could try to find all permutations of [0,1,2,3,4,5,6,7] — that might be algorithmically challenging,
# and would be a brute force way of tackling the problem. We just try everything, and find all possible solutions.

# We’re going to write a “random” algorithm to find solutions to the N queens problem. We’ll begin with the
# permutation [0,1,2,3,4,5,6,7] and we’ll repeatedly shuffle the list, and test each to see if it works!
# Along the way we’ll count how many attempts we need before we find each  solution, and we’ll find 10 solutions
# (we could hit the same solution more than once, because shuffle is random!):


def main():
    import random
    rng = random.Random()
    bd = list(range(8))  # generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1


main()

# On an 8x8 board, there are known to be 92 different solutions to this puzzle. We are randomly picking one of
# 40320 (8!) possible permutations of our representation. So our chances of picking a solution on each try are
# 92/40320. Put another way, on average we’ll need 40320/92 tries — about 438.26 — before we  stumble across
# a solution. The number of tries we printed looks like our experimental data agrees quite nicely with our theory!
