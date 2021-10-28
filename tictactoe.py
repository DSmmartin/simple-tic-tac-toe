import numpy as np


class TicTacToe:

    def __init__(self):
        self.__board = np.empty((3, 3))

    def __show_board(self):
        print(self.__board)  # TODO: improve visualization

    def __run_cycle(self):
        pass

    def __show_winner(self):
        pass

    def start_game(self):
        print('starting game :) ')
        is_finish = False
        while is_finish:
            is_finish = self.__run_cycle()

        self.__show_winner()
