"""Queen chess moves"""

def validate(func):
    """Ensures valid chess positions"""
    def chess_checker(black, white):
        """Ensures valid chess positions"""
        if min(black + white) < 0 or \
           max(black + white) > 7 or \
           black == white:
            raise ValueError
        return func(black, white)
    return chess_checker

@validate
def board(white, black):
    """Prints a board with the queens locations"""
    chess = [["_"] * 8 for _ in range(8)]
    for char, (i, j) in (("W", white), ("B", black)):
        chess[i][j] = char
    return [''.join(row) for row in chess]

@validate
def can_attack(black, white):
    """Checks if the two queens can attack eachother"""
    diff = [abs(b - w) for b, w in zip(black, white)]
    return diff[0] == diff[1] or min(diff) == 0
