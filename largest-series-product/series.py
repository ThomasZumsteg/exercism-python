"""Finds largest product of slices of digits of a give size"""

def largest_product(digits, size):
    """Finds the largest product of slices of a given size"""
    # Why does a blank set of digits have a maximum product of 1?
    slice_list = slices(digits, size)
    def mult_reduce(items):
        total = 1
        for i in items:
            total *= i
        return total
    slice_list = [mult_reduce(l) for l in slice_list]
    return max(slice_list)

def slices(digits, size):
    """Returns list of lists of consecutive digits"""
    if not 0 <= size <= len(digits):
        raise ValueError
    elif digits == '':
        return [[1]]

    slice_list = []

    for i in range(len(digits) - size + 1):
        slice_list.append([int(d) for d in digits[i:i+size]])
    return slice_list
