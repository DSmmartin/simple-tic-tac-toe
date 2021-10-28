import numpy as np

WINNER_STATUS = {1: 'Player 1', 2: 'Player 2', 3: 'draw', 0: None}


class TicTacToe:

    def __init__(self):
        self.__board = np.empty((3, 3))
        self.__winner_status = 0

    def __show_board(self):
        print(self.__board)  # TODO: improve visualization

    def __run_cycle(self):
        self.__winner_status = 3

    def __show_winner(self):
        if (self.__winner_status == 1) | (self.__winner_status == 2):
            print(f'The winner is {WINNER_STATUS.get(self.__winner_status)}')
        elif self.__winner_status == 3:
            print('No winner in this game... :(')

    def start_game(self):
        print('starting game :) ')
        while self.__winner_status == 0:
            self.__run_cycle()

        self.__show_winner()
