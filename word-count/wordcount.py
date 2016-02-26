"""Catalogs and counts the number of words used in a phrase"""
from collections import Counter
import re

def word_count(phrase):
    """Returns dictionary with a count of words used"""
    return Counter(word for word in
        re.split(r'[\W_]+',
                 phrase.lower(), flags=re.UNICODE)
        if word)
