class Cell(object):
    def __init__(self, initial_value):
        self._callbacks = {}

    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        del self._callbacks[callback]


class InputCell(Cell):
    def __init__(self, initial_value):
        self.value = initial_value
        super().__init__(self)


class ComputeCell(Cell):
    def __init__(self, inputs, compute_function):
        self._function = compute_function
        self._inputs = inputs
        self._callbacks = {}
        self._value = None
        super().__init__(self)

    @property
    def value(self):
        new_val = self._function([i.value for i in self._inputs])
        if new_val != self._value:
            self._value = new_val
            for callback in self._callbacks.values():
                callback(new_val)
        return self._value
