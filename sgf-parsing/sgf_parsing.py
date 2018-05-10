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

    def __repr__(self):
        return 'SgfTree({}, [{}])'.format(
                self.properties,
                ','.join(repr(c) for c in self.children))

def parse(input_string):
    stack = []
    state = 'START'
    escape = False
    def raise_error(c):
        raise ValueError(
                "Invalid SgfTree '{}' at '{}' {} '{}'".format(
                    input_string,
                    input_string[:c],
                    input_string[c],
                    input_string[c+1:]))
    for c, char in enumerate(input_string):
        if state == 'START' and char == '(':
            state = 'TREE'
        elif state == 'TREE' and char == ';':
            stack.append(SgfTree())
            state = 'KEY'
            key = ''
        elif state == 'KEY':
            if char == ')' and key and values:
                stack[-1].properties[key] = values
            elif char == '(':
                stack[-1].properties[key] = values
                if len(stack) > 2:
                    node = stack.pop()
                    stack[-1].children.append(node)
            elif char == ';':
                stack[-1].properties[key] = values
                if len(stack) > 1:
                    node = stack.pop()
                    stack[-1].children.append(node)
                stack.append(SgfTree())
                key = ''
            elif char == '[':
                if key == "":
                    raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
                value = ""
                if key not in stack[-1].properties:
                    stack[-1].properties[key] = []
                    values = stack[-1].properties[key]
                state = 'VALUE'
            elif char.islower():
                raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
            else:
                key += char
        elif state == 'VALUE':
            if char == '\\':
                escape = True
            elif not escape and char == ']' and value != "":
                values.append(value)
                value = ""
                state = "KEY"
            elif char == '\t':
                value += ' '
            else:
                value += char
                escape = False
        else:
            raise_error(c)
    if len(stack) == 0:
        raise ValueError("Invalid SgfTree '{}'".format(input_string))
    while len(stack) > 1:
        node = stack.pop()
        stack[-1].children.append(node)
    return stack[0]


