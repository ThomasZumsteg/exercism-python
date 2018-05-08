class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input_string):
    parser = SgfTreeParser(input_string)
    for c in input_string:
        parser.parse(c)
    return parser.result()


class SgfTreeParser(object):
    def __init__(self, input_string):
        self._state = 'START'
        self._root = None
        self._input_string = input_string
        self._states = {
                'START': {
                    '(': self._create_tree
                    }
                }

    def parse(self, char):
        self._states.get(self._state, self._raise_value_error)(char)

    def result(self):
        if self._root is None:
            self._raise_value_error()
        return self._root

    def _raise_value_error(self, *args, **kwargs):
        raise ValueError("Not a valid SgfTree '{}'".format(self._input_string))

    def _create_tree(self, char):
        self._root = SgfTree()
        return self

