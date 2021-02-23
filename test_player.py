import player as p


def test_player_info():
    """tests player info correctly initialized"""
    p1 = p.Player('Ron', 'X', 0)
    assert (p1.name, p1.tile, p1.score) == ('Ron', 'X', 0)


def test_player_name():
    """tests correct name is printed when printing object"""
    p1, ai = p.Player('Harry', 'X', 0), p.Player('Ron', 'O', 0)
    assert p1.__str__() == 'Harry' and ai.__str__() == 'Ron'
