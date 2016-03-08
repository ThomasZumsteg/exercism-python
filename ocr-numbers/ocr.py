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
        '2': [" _ ",
              " _|",
              "|_ ",
              "   "
             ],
        '3': [" _ ",
              " _|",
              " _|",
              "   "
             ],
        '4': ["   ",
              "|_|",
              "  |",
              "   "
             ],
        '5': [" _ ",
              "|_ ",
              " _|",
              "   "
             ],
        '6': [" _ ",
              "|_ ",
              "|_|",
              "   "
             ],
        '7': [" _ ",
              "  |",
              "  |",
              "   "
             ],
        '8': [" _ ",
              "|_|",
              "|_|",
              "   "
             ],
        '9': [" _ ",
              "|_|",
              " _|",
              "   "
             ],
       }

INVERSE_FONT = dict((tuple(v), k) for k, v in FONT.items())

def number(rows):
    """number converts pipes and bars representation of numbers to digits"""
    row_len = len(rows[0])
    if len(rows) != 4 or any(len(row) != row_len for row in rows):
        raise ValueError
    digits = ""
    for n in range(0, row_len, 3):
        digit = [rows[i][n:n+3] for i in range(4)]
        try:
            digits += INVERSE_FONT[tuple(digit)]
        except KeyError:
            digits += "?"
    return digits

def grid(digits):
    """grid converts digits to a pipes and bars representation"""
    grid = ["","","",""]
    for digit in digits:
        try:
            for i, row in enumerate(FONT[digit]):
                grid[i] += row
        except KeyError:
            raise ValueError
    return grid
