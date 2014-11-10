"""Calculates sum and elememts of a geometric series"""

def on_square(n):
    """The nth term of a geometric series"""
    return 2**(n-1)

def total_after(n):
    """The sum of first n terms of a geometric series"""
    # See: http://en.wikipedia.org/wiki/Geometric_progression#Geometric_series
    return 2**n - 1
