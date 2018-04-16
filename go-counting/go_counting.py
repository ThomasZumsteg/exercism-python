from itertools import product

BLACK = "B"
WHITE = "W"
NONE = ""

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self._board = tuple(tuple(row) for row in board)

    def _valid_point(self, x, y):
        return 0 <= y < len(self._board) and 0 <= x < len(self._board[y])

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self._valid_point(x, y):
            raise ValueError("Not on the board ({}, {})".format(x, y))
        owner, group = set(), set()
        queue = [(x, y)]
        while queue:
            x, y = queue.pop()    
            if (x, y) in group or not self._valid_point(x, y):
                continue
            if self._board[y][x] in (BLACK, WHITE):
                owner.add(self._board[y][x])
            elif self._board[y][x] == ' ':
                group.add((x, y))
                queue.extend(((x+1, y), (x-1, y), (x, y+1), (x, y-1)))
        return (owner.pop() if len(owner) == 1 and 0 < len(group) else NONE, group)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        not_seen = set((c, r) for r, row in enumerate(self._board) 
                for c in range(len(row)))
        groups = {BLACK: set(), WHITE: set(), NONE: set()}
        while not_seen:
            x, y = not_seen.pop()
            owner, group = self.territory(x, y)
            not_seen = not_seen - group
            groups[owner].update(group)
        return groups
