from itertools import product

def transpose(input_lines):
    lines = input_lines.splitlines()
    rows, cols = len(lines), max((len(row) for row in lines), default=0)
    result = [[None for _ in range(rows)] for _ in range(cols)]
    for r, c in product(range(rows), range(cols)):
        try:
            char = lines[r][c]
        except IndexError:
            char = ' '
        result[c][r] = char
    return '\n'.join(''.join(row) for row in result)
