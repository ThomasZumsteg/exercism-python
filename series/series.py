"""Finds consecutive number sequences"""

def slices(digits, size):
    """Returns list of lists of consecutive digits"""
    if size <= 0 or size > len(digits):
        raise ValueError

    slice_list = []

    for i in range(len(digits) - size + 1):
        slice_list.append([int(d) for d in digits[i:i+size]])
    return slice_list
