from xogame import board

def test_no_winner_on_empty_board():
    b = board.Board()
    assert b.winner() is None

def test_no_winner_on_incomplete_game():
    b = board.Board()
    b.make_move(what='X', where='a')
    b.make_move(what='O', where='b')
    b.make_move(what='X', where='e')
    assert b.winner() is None
