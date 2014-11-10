"""Catalogs and counts the number of words used in a phrase"""

def word_count(phrase):
    """Returns dictionary with a count of words used"""
    count = {}
    for word in phrase.split():
        try:
            count[word] += 1
        except KeyError:
            count[word] = 1
    return count
