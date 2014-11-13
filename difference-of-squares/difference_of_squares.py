"""Function for calculating squares of sums or sums
of squares and differences between the two
"""
def square_of_sum(num):
    """Square of sum of numbers less then or equal to [num]"""
    return num**2 * (num + 1)**2 // 4

def sum_of_squares(num):
    """Sum of square of numbers less then or equal [num]"""
    return num * (num + 1) * (2 * num + 1) // 6

def difference(num):
    """Difference between the square_of_sums and sum_of_square"""
    return num * (num + 1) * (num - 1) * (3 * num + 2) // 12
