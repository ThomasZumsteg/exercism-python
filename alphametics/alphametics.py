from itertools import permutations

def solve(puzzle):
    words, result = puzzle.split(' == ')
    words = words.split(' + ')
    letters = set(l for word in [result] + words for l in word)
    first_letters = set(w[0] for w in words + [result])

    for combination in combinations(letters, list(range(10))):
        if any(v == 0 and k in first_letters for k, v in combination.items()):
            continue
        if translate(result, combination) == sum(
                translate(word, combination) for word in words):
            return combination

    return {}

def combinations(keys, values):
    for perm in permutations(values, len(keys)):
        yield dict(zip(keys, list(values[p] for p in perm)))

def translate(word, trans):
    result = 0 
    for l in word:
        result = result * 10 + trans[l]
    return result
