def sum_of_multiples(num, multiples=[3,5]):
    """sum_of_multiples sums multiples less than num"""
    return sum(set(n for mul in multiples if mul != 0
               for n in range(0, num, mul)))
