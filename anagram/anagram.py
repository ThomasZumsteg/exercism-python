"""Finds anagrams of a word in a list of words
"""

def detect_anagrams(anagram, word_list):
    """Finds any words in [word_list] that are anagrams of [anagram]"""
    sorted_letters = ''.join(sorted(anagram.lower()))
    anagram_list = []
    for word in word_list:
        # has all the same letters and isn't exactly the target word
        if ''.join(sorted(word.lower())) == sorted_letters and \
           word.lower() != anagram:
            anagram_list.append(word)
    return anagram_list
