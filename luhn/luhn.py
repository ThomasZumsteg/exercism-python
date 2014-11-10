"""Analyzes and creates luhn type codes"""

class Luhn(object):
    """Create and analyze luhn type codes"""

    def __init__(self, number):
        """Initialize a luhn object"""
        self.digits = [int(d) for d in str(number)]

    def addends(self):
        """Does part of the luhn algorythm"""
        ends = []
        for i, digit in enumerate(reversed(self.digits)):
            if i % 2 == 1:
                digit *= 2
            while digit > 10:
                digit -= 9
            ends.insert(0, digit)
        return ends

    def checksum(self):
        """Finds the checksum of the luhn code"""
        return sum(self.addends()) % 10

    def is_valid(self):
        """Checks if luhn code is valid"""
        return 0 == self.checksum()

    @staticmethod
    def create(number):
        """Creates a valid luhn code"""
        code = Luhn(10*number)
        return 10*number + (-code.checksum()) % 10

