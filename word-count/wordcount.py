"""Catalogs and counts the number of words used in a phrase"""
from collections import Counter

def word_count(phrase):
    """Returns dictionary with a count of words used"""
    return Counter(phrase.split())
