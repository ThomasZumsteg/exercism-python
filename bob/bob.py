"""Replys to statements as a lackadaisical teenager would"""

def hey(what):
    """Replys to statements as a lackadaisical teenager would"""
    what = what.strip()
    if what.isupper():
        # Yelling
        return 'Whoa, chill out!'
    elif what.endswith('?'):
        # Question
        return 'Sure.'
    elif what == '':
        # Nothing
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
