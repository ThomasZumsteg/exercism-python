class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self._root = TreeNode(tree_data[0], None, None)
        for data in tree_data[1:]:
            branch = self._root
            while branch is not None:
                root = branch
                attr = 'right' if root.data < data else 'left'
                branch = getattr(root, attr)
            setattr(root, attr, TreeNode(data, None, None))

    def data(self):
        return self._root

    def sorted_data(self):
        result = []
        queue = [self._root]
        while queue:
            node = queue[-1]
            if node.left is not None and node.left not in result:
                queue.append(node.left)
            else:
                result.append(queue.pop())
                if node.right is not None:
                    queue.append(node.right)
        return [n.data for n in result]
