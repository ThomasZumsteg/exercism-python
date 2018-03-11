def is_isogram(string):
    letters = [l.lower() for l in string if l.isalpha()]
    return len(letters) == len(set(letters))
