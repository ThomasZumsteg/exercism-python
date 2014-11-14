"""Sings the beer song"""

def song(*args):
    """Sings the beer song"""
    lyrics = []
    verses = range(*sorted(args))
    for n in reversed(verses + [verses[-1] + 1]):
        lyrics.append(verse(n))
    return "\n".join(lyrics + [''])

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
        return ("%d bottles of beer on the wall, %d bottles of beer.\n"
                "Take one down and pass it around, %d bottles of beer on the wall.\n" % (n, n, n-1))
