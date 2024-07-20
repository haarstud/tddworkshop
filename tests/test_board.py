from xogame import board
import xogame.errors
import pytest

def test_no_winner_on_empty_board():
    b = board.Board()
    assert b.winner() is None

def test_no_winner_on_incomplete_game():
    b = board.Board()
    b.make_move(what='X', where='a')
    b.make_move(what='O', where='b')
    b.make_move(what='X', where='e')
    assert b.winner() is None

def test_X_wins_diagonal():
    b = board.Board()
    b.make_move(what='X', where='a')
    b.make_move(what='O', where='b')
    b.make_move(what='X', where='e')
    b.make_move(what='O', where='d')
    assert b.winner() is None
    b.make_move(what='X', where='i')
    assert b.winner() == 'X'

def test_O_wins_column():
    b = board.Board()
    b.make_move(what='X', where='a')
    b.make_move(what='O', where='b')
    b.make_move(what='X', where='d')
    b.make_move(what='O', where='e')
    b.make_move(what='X', where='c')
    assert b.winner() is None
    b.make_move(what='O', where='h')
    assert b.winner() == 'O'

def test_O_wins_row():
    b = board.Board()
    b.make_move(what='X', where='a')
    b.make_move(what='O', where='d')
    b.make_move(what='X', where='b')
    b.make_move(what='O', where='e')
    b.make_move(what='X', where='g')
    assert b.winner() is None
    b.make_move(what='O', where='f')

    assert b.winner() == 'O'

def test_enforce_players_switching_turns():
    b = board.Board()
    b.make_move(what='X', where='a')
    with pytest.raises(xogame.errors.NotYourTurn):
        b.make_move(what='X', where='b')
        
def test_position_may_only_be_occupied_once():
    b = board.Board()
    b.make_move(what='X', where='a')
    with pytest.raises(xogame.errors.PositionTaken, match='by X'):
        b.make_move(what='O', where='a')
