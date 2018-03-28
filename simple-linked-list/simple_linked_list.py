class Node(object):
    def __init__(self, value):
        self._next = None
        self._value = value

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList(object):
    def __init__(self, values=[]):
        self._len = 0
        self._head = None
        for value in values:
            self.push(value)

    def __len__(self):
        return self._len

    def __iter__(self):
        while self._len > 0:
            yield self.pop()

    def head(self):
        if self._head is None:
            raise EmptyListException("No items in list")
        return self._head

    def push(self, value):
        new_node = Node(value)
        self._len += 1
        new_node._next, self._head = self._head, new_node

    def pop(self):
        old_head, self._head = self.head(), self.head().next()
        self._len -= 1
        return old_head.value()

    def reversed(self):
        return LinkedList(values=self)


class EmptyListException(Exception):
    pass
