from itertools import chain

class CustomSet(object):
    def __init__(self, elements=[]):
        self._store = dict()
        for e in elements:
            self.add(e)

    def isempty(self):
        return len(self._store) <= 0

    def __contains__(self, element):
        return element in self._store

    def issubset(self, other):
        return all(e in other for e in self._store.values())

    def isdisjoint(self, other):
        return not any(e in other for e in self._store.values())

    def __eq__(self, other):
        return self.issubset(other) and other.issubset(self)

    def add(self, element):
        self._store[element] = element

    def intersection(self, other):
        intersection = CustomSet()
        for e in self._store.values():
            if e in other:
                intersection.add(e)
        return intersection

    def __sub__(self, other):
        difference = CustomSet() 
        for e in self._store.values():
            if e not in other:
                difference.add(e)
        return difference

    def __add__(self, other):
        intersection = CustomSet()
        for e in chain(self._store.values(), other._store.values()):
            intersection.add(e)
        return intersection
