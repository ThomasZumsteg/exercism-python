"""Finds the prime factors of a number"""

def prime_factors(number):
    """Finds prime factors of a number"""
    factors = []
    for factor in xrange(2, int(number**0.5)+1):
        while number % factor == 0:
            number /= factor
            factors.append(factor)
            if number == 1:
                break
    if number != 1:
        factors += [number]
    return factors

