"""The method is based on the observation that, for a positive integer n:
    x^n = x * (x^2)^(n-1)/2  if n is odd
        = (x^2)^n/2          if n is even."""


def exp_by_sq(x, n):
    if n < 0:
        return exp_by_sq(1 / x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_sq(x * x, n / 2)
    elif n % 2 != 0:
        return x * exp_by_sq(x * x, (n - 1) / 2)


def exp_by_sq_iter(x, n):
    """The iterative version of algorithm."""
    if n < 0:
        x = 1/x
        n = -n
    if n == 0:
        return 1
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n /= 2
        else:
            y *= x
            x *= x
            n = (n-1)/2
    return x * y


print(exp_by_sq(214, 12))
print(exp_by_sq_iter(214, 12))
