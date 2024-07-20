from xogame import board

def test_no_winner_on_empty_board():
    b = board.Board()
    assert b.winner() is None
