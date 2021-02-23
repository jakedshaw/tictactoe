class Board:
    """Board Class"""

    def __init__(self):
        """initializes board class"""
        self.data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):
        """game board"""
        return f'\n  +-+-+-+   Key' \
               f'\n  |{self.data[0]}|{self.data[1]}|{self.data[2]}|  0|1|2' \
               f'\n  +-+-+-+' \
               f'\n  |{self.data[3]}|{self.data[4]}|{self.data[5]}|  3|4|5' \
               f'\n  +-+-+-+' \
               f'\n  |{self.data[6]}|{self.data[7]}|{self.data[8]}|  6|7|8' \
               f'\n  +-+-+-+'

    def update(self, player, game):
        """updates board and checks for empty cells"""
        if game.next_cell == 'error':
            return False
        elif self.data[game.next_cell] == ' ':
            self.data[game.next_cell] = player.tile
            return True
        else:
            return False

    def check_win(self, player):
        """check for wins"""
        shape = player.tile
        if self.data[0] == shape and self.data[1] == shape and self.data[2] == shape:
            return True
        elif self.data[3] == shape and self.data[4] == shape and self.data[5] == shape:
            return True
        elif self.data[6] == shape and self.data[7] == shape and self.data[8] == shape:
            return True
        elif self.data[0] == shape and self.data[3] == shape and self.data[6] == shape:
            return True
        elif self.data[1] == shape and self.data[4] == shape and self.data[7] == shape:
            return True
        elif self.data[2] == shape and self.data[5] == shape and self.data[8] == shape:
            return True
        elif self.data[0] == shape and self.data[4] == shape and self.data[8] == shape:
            return True
        elif self.data[6] == shape and self.data[4] == shape and self.data[2] == shape:
            return True
        else:
            return False

    def check_full(self):
        """checks if full"""
        if ' ' not in self.data:
            return True
        else:
            return False

    def reset_data(self):
        """resets board"""
        self.data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
