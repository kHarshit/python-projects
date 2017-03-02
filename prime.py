# “Mathematicians have tried in vain to this day to discover some order in the sequence of prime numbers, and
#  we have reason to believe that it is a mystery into which the human mind will never penetrate.”
#                                                                    - Leonhard Euler, 18th century mathematician

def is_prime(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

def primes_by_seive(n):
    out = list()
    sieve = [True] * (n+1)
    for i in range(2, n+1):
        if sieve[i]:
            out.append(i)
            for i in range(i, n+1, i):
                sieve[i] = False
    return out

print(is_prime(11))
print(primes_by_seive(11))


def primes_by_rabin_miller(n):
    """IN production"""
    return False

def is_prime_by_wilson(n): # IN production
    """A simple, but very inefficient primality test uses Wilson's theorem, which states that
     p is prime if and only if: (p-1)! = -1(mod p)"""
    return False

def primes_by_aks_primality_test(n):
    """IN production"""
    return False