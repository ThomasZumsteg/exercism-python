from string import ascii_lowercase as alphabet

def is_pangram(phrase):
    """is_pangram determines if every letter of the alphabet are in a phrase"""
    return all(letter in phrase or letter.upper() in phrase
               for letter in alphabet)
