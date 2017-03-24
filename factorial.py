def factorial(n):
    fact = 1
    if n < 0:
        return "Factorial doesn't exist for negative no!"
    else:
        for i in range(1, n+1):
            fact *= i
            i += 1
        return fact


def fact_rec(n):
    """recursive algorithm"""
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact_rec(n-1)


n = int(input("Enter a no to find its factorial: "))
print(factorial(n))
print(fact_rec(n))
