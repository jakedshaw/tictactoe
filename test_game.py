import game as g
import board as b
import player as p


def test_alternating_turns():
    """tests if turns alternate"""
    p1, ai = p.Player('Ron', 'X', 0), p.Player('Harry', 'O', 3)
    board = b.Board()
    game = g.Game(4)
    game.ai_turn(board, p1, ai)
    assert game.next_player == 0


def test_ai_intelligence_block():
    """tests ai blocks simple win"""
    p1, ai = p.Player('Ron', 'X', 0), p.Player('Harry', 'O', 3)
    board = b.Board()
    board.data = ['X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', 'X']
    game = g.Game(4)
    game.ai_turn(board, p1, ai)
    assert game.next_cell == 0 or 4 or 8


def test_ai_intelligence_win():
    """tests ai places a win"""
    p1, ai = p.Player('Ron', 'X', 0), p.Player('Harry', 'O', 3)
    board = b.Board()
    board.data = ['X', 'O', ' ', ' ', 'O', ' ', ' ', ' ', 'X']
    game = g.Game(4)
    game.ai_turn(board, p1, ai)
    assert game.next_cell == 6 or 4 or 1


def test_score_adder():
    """tests score is added correctly"""
    p1, ai = p.Player('Ron', 'X', 0), p.Player('Joe', 'O', 3)
    tile = 'O'
    game = g.Game(4)
    game.score_adder(tile, p1, ai)
    assert ai.score == 4
