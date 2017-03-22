"""
The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change
 if the larger number is replaced by its difference with the smaller number.
A more efficient version of the algorithm shortcuts these steps, instead replacing the larger of the two numbers by its
remainder when divided by the smaller of the two (with this version, the algorithm stops when reaching a zero remainder)
"""

"""The Euclidean algorithm is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has
 survived to the present day.   - Donald Knuth"""


def gcd(a, b):
    """division based version"""
    while b != 0:
        a, b = b, a % b
    return a


def gcd_sub(a, b):
    """subtraction based version"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def gcd_rec(a, b):
    """recursive version"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(1071, 748))
print(gcd_sub(1071,748))
print(gcd_rec(1071, 748))


# gcd(1071, 748)
#   1071 = 748*1 + 323
#   748 = 323*2 + 102
#   323 = 102*3 + 17   <-- gcd(1071, 748) = 17
#   102 = 17*6 + 0
