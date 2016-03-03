"""Finds primes numbers"""

def sieve(lim):
    """Implimentation of sieve of Eratosthenes"""
    multiples = set()
    primes = [2,]
    for num in range(3, lim+1, 2):
        if num not in multiples:
            primes.append(num)
            multiples.update(range(num**2, lim, num))
    return primes
