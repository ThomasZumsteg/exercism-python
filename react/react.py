CELLS = []

class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        CELLS.append(self)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._value != value:
            self._value = value
            for cell in CELLS:
                cell._update()

    def _update(self):
        return self._value


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self._function = lambda: compute_function([i.value for i in inputs])
        self._callbacks = {}
        self._value = self._function()
        CELLS.append(self)

    @property
    def value(self):
        return self._value

    def _update(self):
        new_val = self._function()
        if new_val != self._value:
            self._value = new_val
            for c in self._callbacks.values():
                c(new_val)
        return new_val

    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        try:
            del self._callbacks[callback]
        except KeyError:
            pass
