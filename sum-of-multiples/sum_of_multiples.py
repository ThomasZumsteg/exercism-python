"""Sums multiples of an arbitrary set of numbers"""

class SumOfMultiples(object):
    """Holds the multiples to preform operations on"""

    def __init__(self, *args):
        """Initilize a set of base numbers,
        3 and 5 unless otherwise specified
        """
        if args == ():
            args = (3, 5)
        self.multiples = args

    def to(self, num):
        """Sums multiples of less then a value"""
        multiple_set = set()
        for mul in self.multiples:
            multiple_set.update(range(0, num, mul))
        return sum(multiple_set)
