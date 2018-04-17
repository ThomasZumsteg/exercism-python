import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real)

    def __sub__(self, other):
        return ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary)

    def __truediv__(self, other):
        common = abs(other) ** 2
        real = self.real * other.real + self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real - self.real * other.imaginary
        return ComplexNumber(real/common, imaginary/common)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
                # Round needed for floating point errors
                round(math.e ** (self.real) * math.cos(self.imaginary), 15),
                round(math.sin(self.imaginary), 15))

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self):
        return "{} + {}i".format(self.real, self.imaginary)
