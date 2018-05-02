class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        self._callbacks = {}

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        print("Updating with {}".format(value))
        if self._value != value:
            self._value = value
            for c in self._callbacks:
                c(value)

    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        del self._callbacks[callback]


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self._value = None
        def compute_val(val):
            new_val = compute_function([i.value for i in inputs])
            if new_val != self._value:
                for c in self._callbacks:
                    c(new_val)
                return new_val
        for i in inputs:
            i.add_callback(compute_val)
        self._function = compute_val
        self._callbacks = {}

    @property
    def value(self):
        new_val = self._function(None)
        if new_val != self._value:
            self._value = new_val
            for callback in self._callbacks.values():
                callback(new_val)
        return self._value

    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        del self._callbacks[callback]
