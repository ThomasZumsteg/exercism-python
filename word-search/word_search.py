from collections import defaultdict
from itertools import product

class Point(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    dirs = tuple(prod for prod in product((0, 1, -1), repeat=2) if prod != (0,0))

    def __init__(self, puzzle):
        hashes = defaultdict(list)
        for r, row in enumerate(puzzle):
            for c, char in enumerate(row):
                start = Point(c, r)
                for word, end in self._words_starting_from(puzzle, start):
                    hashes[word].append((start, end))
        self._hashes = dict(hashes)

    def _words_starting_from(self, puzzle, start):
        char = puzzle[start.y][start.x]
        yield (char, start) 
        queue = [(char, (start.x, start.y), diff) for diff in self.dirs]
        while queue:
            word, pos, diff = queue.pop()
            x, y = (p+d for p, d in zip(pos, diff))
            if 0<= y < len(puzzle) and 0 <= x < len(puzzle[y]):
                word += puzzle[y][x]
                yield(word, Point(x, y))
                queue.append((word, (x, y), diff))

    def search(self, word):
        matches = self._hashes.get(word, [None])
        assert len(matches) == 1
        return matches[0]
