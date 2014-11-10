"""Finds primes numbers"""

def sieve(lim):
    """Implimentation of sieve of Eratosthenes"""
    sieve_list = [True] * lim
    primes = []
    for i in range(2, lim):
        if sieve_list[i]:
            primes.append(i)
            for j in range(2*i, lim, i):
                sieve_list[j] = False
    return primes
