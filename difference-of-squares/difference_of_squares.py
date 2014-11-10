"""Function for calculating squares of sums or sums
of squares and differences between the two
"""
def square_of_sum(num):
    """Square of sum of numbers less then or equal to [num]"""
    return sum(range(1, num+1))**2

def sum_of_squares(num):
    """Sum of square of numbers less then or equal [num]"""
    return sum([x**2 for x in range(1, num+1)])

def difference(num):
    """Difference between the square_of_sums and sum_of_square"""
    return square_of_sum(num) - sum_of_squares(num)
