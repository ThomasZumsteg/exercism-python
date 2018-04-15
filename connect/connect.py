class ConnectGame:
    def __init__(self, board):
        self._board = [line.split() for line in board.splitlines()]
        self._players = {}
        self._players['X'] = (
            tuple((0, r) for r in range(len(self._board))),
            tuple((len(row)-1, r) for r, row in enumerate(self._board)))
        self._players['O'] = (
            tuple((c, 0) for c in range(len(self._board[0]))),
            tuple((c, len(self._board)-1) for c in range(len(self._board[-1]))))

    def get_winner(self):
        for player in self._players.keys():
            if self._find_path(player):
                return player 
        return ''

    def _find_path(self, player):
        start, end = self._players[player]
        """Dijkstras path finding algorithm"""
        queue = list(start)
        seen = set()
        while queue:
            x, y = queue.pop()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            if not (0 <= y < len(self._board) and 0 <= x < len(self._board[y])) or \
                    self._board[y][x] != player:
                continue
            if (x, y) in end:
                return True
            queue.extend((x+r,y+s) for r, s in
                    ((0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1)))
        return False
