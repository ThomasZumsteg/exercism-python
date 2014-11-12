"""A 2 dimentional matrix object"""

class Matrix(object):
    """Creates a 2d matrix object with accessable rows and columns"""

    def __init__(self, matrix):
        """Copy of the input data"""
        self.matrix = matrix

    @property
    def rows(self):
        """Matrix displayed as rows, coumns"""
        if not hasattr(self, '_rows'):
            self._rows = [[int(n) for n in row.split()]
                          for row in self.matrix.split("\n")]
        return self._rows

    @property
    def columns(self):
        """Matrix displayed as columns, rows"""
        if not hasattr(self, '_columns'):
            self._columns = [[] for _ in range(len(self.rows[0]))]
            for row in self.rows:
                for i, item in enumerate(row):
                    self._columns[i].append(item)
        return self._columns
