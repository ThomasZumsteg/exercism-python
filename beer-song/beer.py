"""Sings the beer song"""

def song(start=100, stop=0):
    """Sings the beer song"""
    return "".join(verse(n) + "\n" for n in range(start, stop-1, -1))

def verse(n):
    """Sings a verse of the beer song"""
    if n == 0:
        return ("No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
    if n == 1:
        return ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall.\n")
    if n == 2:
        return ("2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, 1 bottle of beer on the wall.\n")
    else:
        return ("{0} bottles of beer on the wall, {0} bottles of beer.\n"
                "Take one down and pass it around, {1} bottles of beer on the wall.\n".format(n, n-1))
