"""Determines if one list is a sublist of the other"""
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def swapper(func):
    """Wrapper that ensures the first argument is smaller then the seconds"""
    def swap(first, second):
        """swaps first and second argument if the second is smaller"""
        if first == second:
            return EQUAL
        if len(first) > len(second):
            return SUPERLIST * func(second, first)
        else:
            return func(first, second)
    return swap

@swapper
def check_lists(small_list, big_list):
    """Checks if first list is a sublist of the seconds"""
    for i in range(len(big_list) - len(small_list) + 1):
        if small_list == big_list[i: i+len(small_list)]:
            return SUBLIST
    return UNEQUAL

