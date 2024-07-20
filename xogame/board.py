class Board:
    def __init__(self):
        self._board = {position: None for position in 'abcdefghi'}

    def winner(self):
        for symbol in 'XO':
            if self._won(symbol):
                return symbol

        return None

    def _won(self, symbol):
        for row in 'abc', 'def', 'ghi':
            if all(self._board[position] == symbol for position in row):
                return True
        for column in 'adg', 'beh', 'cfi':
            if all(self._board[position] == symbol for position in column):
                return True

        DIAGONAL = 'aei'
        if all(self._board[position] == symbol for position in DIAGONAL):
            return True

        return False

    def make_move(self, what, where):
        self._board[where] = what
