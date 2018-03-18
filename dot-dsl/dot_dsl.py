import functools

NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}, *args):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {} 
        costructors = {
                NODE: self._add_node,
                EDGE: self._add_edge,
                ATTR: self._add_attr,
                }

        for datum in data:
            if type(datum) != tuple or len(datum) < 1:
                raise TypeError("Not a valid entry: {}".format(datum))
            elif datum[0] not in costructors:
                raise ValueError("Not a known type")
            
            costructors[datum[0]](*datum[1:])

    def _add_node(self, *args):
        name, attrs = args
        self.nodes.append(Node(name, attrs=attrs))

    def _add_edge(self, *args):
        src, dst, attrs = args
        self.edges.append(Edge(src, dst, attrs=attrs))

    def _add_attr(self, *args):
        FORMAT = "(ATTR, key, val)"
        if len(args) < 2:
            raise TypeError("{} Not enough args: {}".format(FORMAT, args))
        elif len(args) > 2:
            raise ValueError("{} To many args: {}".format(FORMAT, args))
        self.attrs[args[0]] = args[1]
