"""Finds the largest or smallest palindrome number in range"""

def smallest_palindrome(max_factor=None, min_factor=0):
    """Finds the smallest palindrome number"""
    palindromes = find_panindromes(min_factor, max_factor + 1)
    smallest = min(palindromes)
    return (smallest, palindromes[smallest])

def largest_palindrome(max_factor=None, min_factor=0):
    """Finds the largest palindrome number"""
    palindromes = find_panindromes(min_factor, max_factor + 1)
    largest = max(palindromes)
    return (largest, palindromes[largest])

def find_panindromes(start, stop):
    """Finds palindrome numbers"""
    palindromes = {}
    for a in range(start, stop):
        for b in range(a, stop):
            prod = a*b
            if str(prod) == str(prod)[::-1]:
                palindromes[prod] = {a, b}
    return palindromes
