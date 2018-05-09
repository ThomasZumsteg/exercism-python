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
    queue = []
    state = 'NEW'
    for c, char in enumerate(input_string):
        if state == 'NEW':
            if char == '(':
                state = 'TREE'
                node = SgfTree()
            else:
                raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
        elif state == 'TREE':
            if char == ';':
                state = 'KEY'
                key = ''
            else:
                raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
        elif state == 'KEY':
            if char == ')':
                if key == "":
                    queue.append(node)
                else:
                    raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
            elif char == '[':
                if key == "":
                    raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
                value = ""
                values = []
                state = 'VALUE'
            elif char.islower():
                raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
            else:
                key += char
        elif state == 'VALUE':
            if char == ']':
                if value != "":
                    values.append(value)
                    value = ""
                else:
                    raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
            elif char == ')':
                node.properties[key] = values
                queue.append(node)
            else:
                value += char
        else:
            raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
    if len(queue) != 1:
        raise ValueError("Invalid SgfTree '{}'".format(input_string))
    return queue[0]


