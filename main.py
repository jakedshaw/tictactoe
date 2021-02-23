import player as p
import board as b
import game as g
from os import system


def clear():
    """clears terminal"""
    _ = system('clear')


def welcome_message():
    """welcome message"""
    print("Welcome to Tic-Tac-Toe!\n\n"
          "This is a one-player game against a computer opponent.\n\n"
          "Press ENTER to start ('q' to quit) ", end='')
    i = input()
    if i == 'q':
        clear()
        quit()
    elif i == '':
        clear()
    else:
        clear()
        welcome_message()


def continue_game():
    """main menu"""
    print(f"Press ENTER to Continue ", end='')
    i = input()
    if i == 'q':
        clear()
        quit()
    elif i == '':
        clear()
    else:
        continue_game()


def game_number():
    """asks how many games"""
    print('How many games do you want to play? ', end='')
    a = input()
    if a == '':
        clear()
        return game_number()
    else:
        try:
            a = int(a)
            if a > 0:
                return a
            elif a == 0:
                clear()
                quit()
            else:
                clear()
                return game_number()
        except ValueError:
            clear()
            return game_number()


def name_asker():
    """asks for name"""
    print('\nWhat is your name? ', end='')
    return input()


def initialize():
    """initializes objects"""
    gam, boar = g.Game(game_number()), b.Board()
    pla, art = p.Player(name_asker(), 'X', 0), p.Player('Opponent', 'O', 0)
    return gam, boar, pla, art


def run_game():
    """game instructions"""
    player = p1
    while not board.check_win(player):
        if board.check_full():
            break
        game.next_cell, z = 'error', 0
        if game.next_player == 0:
            while not board.update(p1, game):
                if z >= 1:
                    print('\nSpot taken, try somewhere else.')
                game.p1_turn(board, p1.name)
                player = p1
                z += 1
        if not board.check_win(player):
            if not board.check_full():
                game.next_cell = 'error'
                if game.next_player == 1:
                    while not board.update(ai, game):
                        game.ai_turn(board, p1, ai)
                        player = ai
    if board.check_full() and not board.check_win(player):
        game.score_adder(' ', board, p1, ai)
        board.reset_data()
    else:
        game.score_adder(player.tile, board, p1, ai)
        board.reset_data()


if __name__ == '__main__':
    clear()
    while True:
        welcome_message()
        game, board, p1, ai = initialize()
        while game.number >= 1:
            run_game()
            if game.number >= 1:
                continue_game()
