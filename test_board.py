import board as b
import player as p


def test_win():
    """tests for win"""
    board = b.Board()
    p1 = p.Player('Ron', 'X', 0)
    board.data = [' ', ' ', 'O', 'O', ' ', 'O', 'X', 'X', 'X']
    assert board.check_win(p1) == True


def test_tie():
    """tests for tie and not win"""
    board = b.Board()
    p1 = p.Player('Ron', 'X', 0)
    board.data = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
    assert board.check_full() == True and board.check_win(p1) == False


def test_reset_board():
    """tests board resets"""
    board = b.Board()
    board.data = [' ', ' ', 'O', 'O', ' ', 'O', 'X', 'X', 'X']
    board.reset_data()
    assert board.data == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
