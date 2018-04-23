class Zipper(object):
    @staticmethod
    def from_tree(tree):
        return Zipper(tree, tuple())

    def __init__(self, tree, crumbs):
        self.tree = tree
        self.crumbs = crumbs

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        root = {
            'left': self.tree['left'],
            'right': self.tree['right'],
            'value': value
            }
        return Zipper(root, self.crumbs)

    def left(self):
        if self.tree['left']:
            right = ('left', self.tree['value'], self.tree['right'])
            return Zipper(self.tree['left'], self.crumbs + (right,))

    def set_left(self, left):
        root = {
            'left': left,
            'right': self.tree['right'],
            'value': self.tree['value']
            }
        return Zipper(root, self.crumbs)

    def right(self):
        if self.tree['right']:
            left = ('right', self.tree['value'], self.tree['left'])
            return Zipper(self.tree['right'], self.crumbs + (left,))

    def set_right(self, right):
        root = {
            'left': self.tree['left'],
            'right': right,
            'value': self.tree['value']
            }
        return Zipper(root, self.crumbs)

    def up(self):
        if len(self.crumbs) <= 0:
            return None
        direcion, value, tree = self.crumbs[-1]
        root = {
            'value': value,
            direcion: self.tree,
            'left' if direcion == 'right' else 'right': tree}
        return Zipper(root, self.crumbs[:-1])

    def to_tree(self):
        stepUp = self.up()
        if stepUp is None:
            return self.tree
        return stepUp.to_tree()
