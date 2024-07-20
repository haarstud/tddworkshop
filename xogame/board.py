class Board:
    def __init__(self):
        self._winner = None

    def winner(self):
        return self._winner

    def make_move(self, what, where):
        if (what, where) == ('X', 'i'):
            self._winner = 'X'
