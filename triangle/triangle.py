"""Validate and specify triangle types"""

class TriangleError(Exception):
    """Error if it cannot be a triangle"""
    def __init__(self, message):
        super(TriangleError, self).__init__(message)

class Triangle(object):
    """Validate and specify triangle types"""
    def __init__(self, a, b, c):
        """Create and validate triangle"""
        (self.a, self.b, self.c) = sorted((a, b, c))
        if self.a + self.b <= self.c:
            raise TriangleError("Not a Triangle")

    def kind(self):
        """Specify triangle type"""
        if self.a == self.b and self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c:
            return "isosceles"
        else:
            return "scalene"
