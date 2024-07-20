from . import errors

class Board:
    def __init__(self):
        self._board = {position: None for position in 'abcdefghi'}
        self._last_player = None

    def winner(self):
        for symbol in 'XO':
            if self._won(symbol):
                return symbol

        return None

    def _won(self, symbol):
        COLUMNS = ['adg', 'beh', 'cfi']
        ROWS = ['abc', 'def', 'ghi']
        DIAGONAL = 'aei'
        WINNING_COMBINATIONS = ROWS + COLUMNS + [DIAGONAL]
        for combination in WINNING_COMBINATIONS:
            if all(self._board[position] == symbol for position in combination):
                return True

        return False

    def make_move(self, what, where):
        self._enforce_valid_move(what, where)
        self._last_player = what
        self._board[where] = what

    def _enforce_valid_move(self, what, where):
        if what not in 'XO':
            raise errors.InvalidSymbol(f'what must be X or O, not {what}')
        if where not in self._board.keys():
            raise errors.InvalidPosition(f'position {where} is not valid')

        if self._board[where] is not None:
            raise errors.PositionTaken(f'position {where} is already taken by {self._board[where]}')

        if self._last_player == what:
            raise errors.NotYourTurn
