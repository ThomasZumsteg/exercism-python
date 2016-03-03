from re import search

def translate(phrase):
    """translate converts a phrase to piglatin"""
    return ' '.join(translate_word(word) for word in phrase.split())

CASES = ( r'(.*?[^q])(u.*)', # q case
         r'(^y[^aeiou].*)()', # y case
         r'(.*?)([aeoi].*)' ) # default case

def translate_word(word):
    """translate_word converts a word to piglatin"""
    for case in CASES:
        match = search(case, word)
        if match and match.group(1) + "ay" != word:
            return match.group(2) + match.group(1) + "ay"
    return word + "ay"
