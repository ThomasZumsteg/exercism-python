"""Finds anagrams of a word in a list of words"""

def detect_anagrams(anagram, word_list):
    """Finds any words in [word_list] that are anagrams of [anagram]"""
    letters = sorted(anagram.lower())
    return [word for word in word_list
            if sorted(word.lower()) == letters
            and word.lower() != anagram.lower()]
