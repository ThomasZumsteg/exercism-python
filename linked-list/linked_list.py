class Node(object):
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class LinkedList(object):
    def __init__(self):
        self.head = None
        self._len = 0

    def __len__(self):
        # faster than len(list(iter(self))) but requires keeping _len updated
        return self._len

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p.previous.value
            p = p.previous
            if p == self.head:
                return

    def push(self, value):
        self._len += 1
        node = Node(value)
        if self.head == None:
            self.head = node.next = node.previous = node
        else:
            node.next, node.previous = self.head, self.head.previous
            self.head.previous.next = self.head.previous = self.head = node

    def pop(self):
        self._len -= 1
        node = self.head
        if self.head.next == self.head:
            self.head = None # Last item
        else:
            node.previous.next = self.head = node.next
            self.head.previous = node.previous
        return node.value

    def shift(self):
        self.head = self.head.previous
        value = self.pop()
        return value

    def unshift(self, value):
        if self.head is not None:
            self.head = self.head.previous
        self.push(value)
        self.head = self.head.next
