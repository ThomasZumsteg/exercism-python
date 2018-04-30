from json import dumps
from itertools import chain

class Tree(object):
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        steps = self.find(from_node)
        for step in steps[1:]:
            self.children = [c for c in self.children if c.label != step.label]
            step.label, self.label = self.label, step.label
            step.children, self.children = self.children, step.children
            self.children.append(step)
        return self

    def path_to(self, from_node, to_node):
        to_path, from_path = self.find(to_node), self.find(from_node)
        return list(n.label for n in chain(reversed(from_path), to_path[1:]))

    def find(self, to_node):
        queue = [(self, tuple())]
        while queue:
            node, path = queue.pop()
            path += (node,)
            if node.label == to_node:
                return path
            queue.extend((c, path) for c in node.children)
        raise ValueError("No node {}".format(to_node))
