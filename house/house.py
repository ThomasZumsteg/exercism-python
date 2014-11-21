"""Recites 'This is the House that Jack Built'"""

def rhyme():
    """Recites the entire rhyme"""
    return "\n\n".join(verse(n) for n in range(1, 13))

def verse(v):
    """Recites a verse"""
    verses = ["the horse and the hound and the horn\nthat belonged to ",
              "the farmer sowing his corn\nthat kept ",
              "the rooster that crowed in the morn\nthat woke ",
              "the priest all shaven and shorn\nthat married ",
              "the man all tattered and torn\nthat kissed ",
              "the maiden all forlorn\nthat milked ",
              "the cow with the crumpled horn\nthat tossed ",
              "the dog\nthat worried ",
              "the cat\nthat killed ",
              "the rat\nthat ate ",
              "the malt\nthat lay in ",
              "the house that Jack built.",
             ]
    return ''.join(["This is "] + verses[-v:])
