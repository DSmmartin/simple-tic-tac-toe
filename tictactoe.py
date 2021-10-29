import numpy as np

WINNER_STATUS = {1: 'Player 1', 2: 'Player 2', 3: 'draw', 0: None}


class TicTacToe:
    _board = np.empty((3, 3))
    _winner_status = 0
    _iteration = 0

    def __show_board(self):
        print(f'-- Board at iteration: {self._iteration}')
        print(self._board)  # TODO: improve visualization

    def __run_cycle(self):
        self._winner_status = 3

    def __show_winner(self):
        if (self._winner_status == 1) | (self._winner_status == 2):
            print(f'The winner is {WINNER_STATUS.get(self._winner_status)}')
        elif self._winner_status == 3:
            print('No winner in this game... :(')

    def start_game(self):
        print('starting game :) ')
        self.__show_board()
        while self._winner_status == 0:
            self.__run_cycle()
            self._iteration += 1
            self.__show_board()

        self.__show_winner()
