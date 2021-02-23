from random import choice
from os import system
import numpy as np


class Game:
    """Game Class"""

    def __init__(self, number):
        """initializes game class"""
        self.number = number
        self.next_cell = 'error'
        self.next_player = choice([0, 1])

    def __str__(self):
        """prints how many games left"""
        if self.number == 0:
            return 'info'
        elif self.number == 1:
            return '1 game left!'
        else:
            return f'{self.number} games left!'

    def p1_turn(self, board, name):
        """player's turn"""
        clear()
        print(f'Hi {name}, you are X')
        print(board)
        print('\nWhere do you want to play? (0-8) ', end='')
        cell = input()
        try:
            cell = int(cell)
            if cell > 8:
                print('Must be integer from (0-8)')
                self.p1_turn(board, name)
            elif cell < 0:
                print('Must be integer from (0-8)')
                self.p1_turn(board, name)
            else:
                self.next_cell = cell
                self.next_player = 1
        except ValueError:
            self.p1_turn(board, name)

    def ai_turn(self, board, p1, ai):
        """intelligent-ish ai"""
        b = np.reshape(board.data, (3, 3))
        self.next_player = 0  # p1 turn next
        a = [0, 0, 0, 0, 0, 0, 0, 0]
        for j in [p1.tile, ai.tile, ' ']:
            for i in range(3):
                if b[0, i] == j:
                    a[0] += 1
                if b[1, i] == j:
                    a[1] += 1
                if b[2, i] == j:
                    a[2] += 1
                if b[i, 0] == j:
                    a[3] += 1
                if b[i, 1] == j:
                    a[4] += 1
                if b[i, 2] == j:
                    a[5] += 1
                if b[i, i] == j:
                    a[6] += 1
                if b[2-i, i] == j:
                    a[7] += 1
            if j == p1.tile:
                c = a
                a = [0, 0, 0, 0, 0, 0, 0, 0]
            elif j == ai.tile:
                d = a
                a = [0, 0, 0, 0, 0, 0, 0, 0]
            elif j == ' ':
                e = a
                a = [0, 0, 0, 0, 0, 0, 0, 0]
            else:
                clear()
                print('error 1')
                quit()
        a, x, y = c, 'go', 'first'
        while not x == 'end':
            x = 'end'
            if a[0] == 2 and e[0] == 1:
                self.next_cell = choice([0, 1, 2])
            elif a[1] == 2 and e[1] == 1:
                self.next_cell = choice([3, 4, 5])
            elif a[2] == 2 and e[2] == 1:
                self.next_cell = choice([6, 7, 8])
            elif a[3] == 2 and e[3] == 1:
                self.next_cell = choice([0, 3, 6])
            elif a[4] == 2 and e[4] == 1:
                self.next_cell = choice([1, 4, 7])
            elif a[5] == 2 and e[5] == 1:
                self.next_cell = choice([2, 5, 8])
            elif a[6] == 2 and e[6] == 1:
                self.next_cell = choice([0, 4, 8])
            elif a[7] == 2 and e[7] == 1:
                self.next_cell = choice([6, 4, 3])
            elif y == 'first':
                x, a, y = 'go', d, 'second'
            elif y == 'second':
                x, y = 'go', 'first'
                while not x == 'end':
                    x = 'end'
                    if a[0] == 1 and e[0] == 2:
                        self.next_cell = choice([0, 1, 2])
                    elif a[1] == 1 and e[0] == 2:
                        self.next_cell = choice([3, 4, 5])
                    elif a[2] == 1 and e[0] == 2:
                        self.next_cell = choice([6, 7, 8])
                    elif a[3] == 1 and e[0] == 2:
                        self.next_cell = choice([0, 3, 6])
                    elif a[4] == 1 and e[0] == 2:
                        self.next_cell = choice([1, 4, 7])
                    elif a[5] == 1 and e[0] == 2:
                        self.next_cell = choice([2, 5, 8])
                    elif a[6] == 1 and e[0] == 2:
                        self.next_cell = choice([0, 4, 8])
                    elif a[7] == 1 and e[0] == 2:
                        self.next_cell = choice([6, 4, 3])
                    elif y == 'first':
                        x, y, a = 'go', 'second', c
                    elif y == 'second':
                        self.next_cell = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
                    else:
                        clear()
                        print('error 3')
                        quit()
            else:
                clear()
                print('error 2')
                quit()

    def score_adder(self, tile, board, p1, ai):
        """adds score & determines to continue or end"""
        if tile == 'X':
            p1.score += 1
            a = 'Won!'
        elif tile == 'O':
            ai.score += 1
            a = 'Lost.'
        else:
            a = 'Tied'
        clear()
        self.number -= 1
        if self.number == 0:
            if p1.score > ai.score:
                print(f'You Won! {p1.score}:{ai.score}')
            elif ai.score > p1.score:
                print(f'Better luck next time. {p1.score}:{ai.score}')
            else:
                print(f"It's a draw. {p1.score}:{ai.score}")
        elif self.number == 1:
            print(f'Round {a} 1 game left!')
        else:
            print(f'Round {a} {p1.score}:{ai.score}\n\n{self.number} games left!')
        print('\n', board, '\n')


def clear():
    """clears terminal"""
    _ = system('clear')
