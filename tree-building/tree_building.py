from collections import defaultdict

class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    nodes = {}
    parent_tree = defaultdict(list)

    for j in records:
        if (j.record_id == j.parent_id != 0) or j.record_id < j.parent_id:
            raise ValueError("Invalid record {}".format(j))
        node = Node(j.record_id)
        nodes[j.record_id] = node
        if node.node_id != 0:
            parent_tree[j.parent_id].append(node)

    if nodes == {}:
        return None
    elif 0 not in nodes:
        raise ValueError("No root node")
    elif len(nodes) - 1 != max(nodes.keys()):
        raise ValueError("To many nodes")

    for pid, children in parent_tree.items():
        children.sort(key=lambda n: n.node_id)
        nodes[pid].children.extend(children)
    return nodes[0]
