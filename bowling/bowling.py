from itertools import zip_longest

class BowlingGame(object):
    def __init__(self):
        self._rolls = []
        self._frame = 0
        self._first = True
        self._extra_rolls = None

    def roll(self, pins):
        if self._game_over():
            raise IndexError("Game Over")
        elif not (0 <= pins <= 10):
            raise ValueError("Cannot score {}".format(pins))
        elif not self._first and pins + self._rolls[-1] > 10:
            raise ValueError("Cannot score {} and {}".format(self._rolls[-1], pins))

        self._rolls.append(pins)
        self._update_state()

    def score(self):
        if not self._game_over():
            raise IndexError("Game in progress")

        index, frame, total = 0, 0, 0
        while index < len(self._rolls) and frame < 10:
            first, second, third = (self._rolls[i] if i < len(self._rolls) else 0 
                for i in range(index, index+3))

            strike, spare = first == 10, first + second == 10

            total += first + second + (third if (strike or spare) else 0)
            index += 1 if strike else 2
            frame += 1
        return total

    def _update_state(self):
        strike = self._rolls[-1] == 10

        self._frame = min(20, self._frame + (2 if strike else 1))
        self._first = True if strike else not self._first

        if 20 == self._frame and self._extra_rolls is None: 
            self._extra_rolls = 0
            if strike:
                self._extra_rolls = 2
            elif sum(self._rolls[-2:]) == 10:
                self._extra_rolls = 1
        elif self._extra_rolls is not None:
            self._extra_rolls -= 1

    def _game_over(self):
        return not (self._frame < 20 or 0 < self._extra_rolls)
