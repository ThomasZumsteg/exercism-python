"""Transforms an old data structure into a new one"""

def transform(old_structure):
    """Swaps key and value in old data structure"""
    new_structure = {}
    for key, items in old_structure.iteritems():
        for item in items:
            new_structure[item.lower()] = key
    return new_structure
