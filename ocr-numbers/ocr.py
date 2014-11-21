"""Converts digits to a grid font"""

FONT = {'0': [" _ ",
              "| |",
              "|_|",
              "   "
             ],
        '1': ["   ",
              "  |",
              "  |",
              "   "
             ],
       }

INVERSE_FONT = dict((tuple(v), k) for k, v in FONT.iteritems())

def number(num):
    """Convert a string of characters into a single digiti"""
    if len(num) != 4 or not all(len(row) == 3 for row in num):
        raise ValueError
    try:
        return INVERSE_FONT[tuple(num)]
    except KeyError:
        return "?"

def grid(num):
    """Convert a digit into a ocr digit"""
    return FONT[num]
