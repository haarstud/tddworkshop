import xogame.player


def launch_server():
    return 'http://localhost:5000'
    
def winner():
    return None

def test_xogame():
    user_x = xogame.player.Player('X')
    user_o = xogame.player.Player('O')

    server_url = launch_server()
    user_x.connect(server_url)
    user_o.connect(server_url)

    user_x.make_move('a')
    assert winner() is None
    user_o.make_move('b')
    assert winner() is None
    user_x.make_move('e')
    assert winner() is None
    user_o.make_move('d')
    assert winner() is None
    user_x.make_move('i')
    assert winner() is 'X'
