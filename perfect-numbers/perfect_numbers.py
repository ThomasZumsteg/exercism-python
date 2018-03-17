from itertools import count

def classify(number):
    factor_sum = sum(factor_gen(number))
    # Switch
    if factor_sum == number:
        return "perfect"
    elif factor_sum < number:
        return "deficient"
    elif factor_sum > number:
        return "abundant"
    # Oops

def factor_gen(number):
    """
    Factors that evenly divide some number and are not equal to the number 
    
    ex:
        factors(0) = ValueError # Numbers zero or less have no factors
        factors(1) = []
        factors(2) = [1]
        factors(42) = [1, 2, 3, 6, 7, 14, 21]
    """
    if number <= 0:
        raise ValueError("Not a valid number {}".format(number))
    # O(sqrt(n)) sorted solution
    # For the unsorted solution, remove the queue and yield when found
    queue = []
    for f in count(1):
        if number != 1 and (f == 1 or f * f == number):
            yield f
        elif number <= f * f:
            yield from iter(queue)
            raise StopIteration
        elif number % f == 0:
            yield f
            queue.insert(0, number // f)
