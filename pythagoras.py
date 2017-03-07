import timeit

def pythagorean_triplets(n):
    """Note that this algorithm is not efficient"""
    for x in range(n):
        for y in range(x+1, n):
            for z in range(y+1, n):
                if x*x + y*y == z*z:
                    print(x, y, z)

def pythagorean_triplets_eff(n):
    for x in range(n):
        for y in range(x+1, n):
            z = y + 1
            while z*z < x*x + y*y:
                z += 1
            if z*z == x*x + y*y:
                print(x, y, z)

def pythagorean_triplets_efficient(n):
    """It is an efficient algorithm to find pythagorean triplets"""
    for x in range(1, n):
        y = x + 1
        z = y + 1
        while z <= n:
            while z*z < x*x + y*y:
                z += 1
            if z*z == x*x + y*y:
                print(x, y, z)
            y += 1


n = int(input("Enter n to print pythagorean triplets upto n: "))

t0 = timeit.default_timer()
pythagorean_triplets(n)
t1 = timeit.default_timer()
print("\n", t1 - t0)

t2 = timeit.default_timer()
pythagorean_triplets_eff(n)
t3 = timeit.default_timer()
print("\n", t3 - t2)

t4 = timeit.default_timer()
pythagorean_triplets_efficient(n)
t5 = timeit.default_timer()
print(t5 - t4)
