from itertools import combinations
from re import match

def count(diagram=""):
    """count find the number of rectangles in a given diagram"""
    corners = find_char(diagram, '+')
    return sum(1 for rect in combinations(corners, 4) if is_rect(rect, diagram))

def find_char(lines, char):
    """find_char returns the location of all the corner characters"""
    return [ (row, col)
        for row, line in enumerate(lines)
        for col, elem in enumerate(line)
        if elem == char]

def is_rect(corners, diagram):
    """is_rect determines if a set of corners is a rectangle
    by checking alignment and characters between the corners"""
    (a_r, a_c), (b_r, b_c), (c_r, c_c), (d_r, d_c) = sorted(corners)
    if not (a_r == b_r and a_c == c_c and b_c == d_c and c_r == d_r):
        return False

    horz_regex = '\+[-+]{{{}}}\+'.format( d_c - a_c - 1)
    vert_regex = '\+[|+]{{{}}}\+'.format( d_r - a_r - 1)
    top = ''.join(diagram[a_r][a_c:(d_c+1)])
    bottom = ''.join(diagram[d_r][a_c:(d_c+1)])
    left = ''.join(row[a_c] for row in diagram[a_r:(d_r+1)])
    right = ''.join(row[d_c] for row in diagram[a_r:(d_r+1)])

    return match(horz_regex, top) and match(horz_regex, bottom) and \
        match(vert_regex, right) and match(vert_regex, left)
