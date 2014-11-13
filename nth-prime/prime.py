"""Finds the nth prime number"""

def nth_prime(nth):
    """Returns the nth prime number"""
    for mth, prime in enumerate(prime_gen(), 1):
        if mth == nth:
            return prime

def prime_gen():
    """A continaully updating prime number generator"""
    yield 2 # Skips even number for speed
    (start, stop) = (3, 5)
    primes = []
    multiples = set()
    while True:
        # Wheel
        for prime in primes:
            # multiples of prime, from smallest larger then start to stop
            multiples.update(range((-start) % prime + start, stop, prime))
        # Sieve
        for num in xrange(start, stop, 2):
            if num not in multiples:
                yield num
                primes.append(num)
                multiples.update(range(num**2, stop, num))
         # doubles the range, but always to an odd number
        (start, stop) = (stop, stop * 2 - 1)
