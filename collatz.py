# The Collatz conjecture is a conjecture in mathematics named after Lothar Collatz.
# The conjecture is also known as the "3n + 1 conjecture".

# The conjecture can be summarized as follows:
# Take any positive integer n. If n is even, divide it by 2 to get n / 2.
# If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
# Repeat the process (which has been called "Half Or Triple Plus One", or HOTPO[7]) indefinitely.
# The conjecture is that no matter what number you start with, you will always eventually reach 1.


def collatz_conjecture(n):
    """Print the 3n+1 sequence from n, terminating when it reaches 1"""
    seq = [n]
    if n < 1:
        return []
    while n > 1:
        # print(n, end=', ')
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1
        seq.append(n)
    return seq


print(collatz_conjecture(12))