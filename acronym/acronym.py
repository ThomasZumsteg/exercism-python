from re import split

def abbreviate(phrase):
    """abbreviate creates an acronym for a phrase"""
    return ''.join(abbreviate_word(word) for word in split('\W+', phrase))

def abbreviate_word(word):
    """abbreviate_word selects the letters in a word to use for abbriviation"""
    if all(letter.isupper() for letter in word):
        return word[0]
    return word[0].upper() + ''.join(letter for letter in word[1:] if letter.isupper())
