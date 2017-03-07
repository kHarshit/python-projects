def fibonacci(n):
    a, b = 1, 1
    for i in range(n-1):
        # print(a, end=' ')
        a, b = b, a+b
    return a


# def fib_generator(n):
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a+b

# f = fib_generator()
# for i in range(6):
#     print(f.next())



numFibCalls_rec = 0
def fibonacci_rec(n):
    """This algorithm is inefficient because it recalculates the same value many times"""
    global numFibCalls_rec
    numFibCalls_rec += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


numFibCalls_memoize = 0
def fib_memoization(n, dict):
    """It is an efficient algorithm as it first lookup if value is already calculated"""
    global numFibCalls_memoize
    numFibCalls_memoize += 1
    if n in dict:
        return dict[n]
    else:
        ans = fib_memoization(n - 1, dict) + fib_memoization(n - 2, dict)
        dict[n] = ans
        return ans

d = {1:1, 2:1}


n = int(input("Enter n to find nth fibonacci number: "))
print("fibonacci num:", fibonacci(n))
# print("fibonacci num:", fib_generator(n), ", numFibCalls:", )
print("fibonacci num:", fibonacci_rec(n), ", numFibCalls_rec:", numFibCalls_rec)
print("fibonacci num:", fib_memoization(n, d), ", numFibCalls_memoize:", numFibCalls_memoize)
