"""Fills in number on a minesweeper board"""

from re import match

def validate_and_format(func):
    """Finds bad boards and formats function return"""
    def minesweeper(minefield):
        """Finds bad boards and formats function returns"""
        width = len(minefield[0])
        row_regex = r'^\|[* ]{%d}\|$' %(width-2)
        cap_regex = r'^\+-{%d}\+$' %(width-2)
        if not all(match(row_regex, row) for row in minefield[1:-1]) or \
           not match(cap_regex, minefield[0]) or \
           not match(cap_regex, minefield[-1]):
            raise ValueError
        minefield = [list(row) for row in minefield]
        return [''.join(row) for row in func(minefield)]
    return minesweeper

@validate_and_format
def board(minefield):
    """Fills in numbers on a minesweeper board"""
    for i, row in enumerate(minefield[1:-1], 1):
        for j, char in enumerate(row[1:-1], 1):
            if char == "*":
                update(minefield, i, j)
    return minefield

def update(field, row, col):
    """Updates a set of 9 cells"""
    # Uses pass by reference (sort of)
    for m in range(row-1, row+2):
        for n in range(col-1, col+2):
            if field[m][n] == ' ':
                field[m][n] = '1'
            elif field[m][n].isdigit():
                field[m][n] = str(int(field[m][n]) + 1)
