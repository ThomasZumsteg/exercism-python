"""Finds saddle points in a rectangular 2d array"""

def saddle_points(matrix):
    """Finds points that are the largest in their row
    and smallest in their column
    """
    saddles = set()
    min_col = {}
    for r, row in enumerate(matrix):
        max_row = max(row)
        for c in range(len(row)):
            if c not in min_col:
                try:
                    min_col[c] = min(_row[c] for _row in matrix)
                except IndexError:
                    raise ValueError
            if max_row == min_col[c]:
                saddles.add((r, c))
    return saddles
