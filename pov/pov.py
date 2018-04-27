from json import dumps

class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        path = self.path_to(self.label, from_node)
        for step in path[1:]:
            pass
        return self

    def path_to(self, from_node, to_node):
        queue = [(self, tuple())]
        to_path, from_path = None, None
        while to_path is None or from_path is None:
            try:
                node, path = queue.pop()
            except IndexError:
                raise ValueError("No path from {} to {}".format(from_node, to_node))
            path += (node.label,)
            if node.label == from_node:
                from_path = path
            if node.label == to_node:
                to_path = path
            queue.extend((c, path) for c in node.children)
        return list(reversed(from_path)) + list(to_path[1:])
