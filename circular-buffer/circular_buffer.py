class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._items = list()

    def read(self):
        try:
            return self._items.pop(0)
        except IndexError as e:
            raise BufferEmptyException(
                    "Empty buffer: CircularBuffer({})".format(self._capacity)
                    ) from e

    def write(self, data):
        if self._full():
            raise BufferFullException(
                    "Buffer is full: CircularBuffer({})".format(self._capacity))
        self._items.append(data)

    def overwrite(self, data):
        if self._full():
            self.read()
        self.write(data)

    def clear(self):
        self._items = []

    def _full(self):
        return len(self._items) >= self._capacity
