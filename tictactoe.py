"""Objects required to play TicTacToe game
"""
import random
import numpy as np


WINNER_STATUS = {1: 'Player 1', 2: 'Player 2', 3: 'draw', 0: None}


class TicTacToe:
    _length = 3
    _winner_status = 0
    _iteration = 0

    def __init__(self) -> None:
        self._board = np.empty((self._length, self._length), dtype='<U1')
        self._board[:] = '-'

    def __str__(self) -> str:
        return """
        The game of TicTacToe.
        Instructions link: https://en.wikipedia.org/wiki/Tic-tac-toe
        """

    def __show_board(self):
        print(f'-- Board at iteration: {self._iteration}')
        print(self._board)  # TODO: improve visualization

    def __run_cycle(self):
        self._winner_status = 1

    def __show_winner(self):
        if (self._winner_status == 1) | (self._winner_status == 2):
            print(f'The winner is {WINNER_STATUS.get(self._winner_status)}')
        elif self._winner_status == 3:
            print('No winner in this game... :(')

    def __check_if_filled(self):
        return '-' not in self._board

    def __check_winner(self):
        for line in self._length:
            self._board[:, line]
            self._board[line, :]

    def start_game(self):
        print('starting game :) ')
        self.__show_board()
        while self._winner_status == 0:
            self.__run_cycle()
            self._iteration += 1
            self.__show_board()
            if self.__check_if_filled():
                self._winner_status = 3

        self.__show_winner()


class Player:
    def make_a_move(self, position: int):
        return position


class HumanPlayer(Player):
    def make_a_move(self):
        position = int(input())  # TODO: make more robust
        return super().make_a_move(position)


class IAPlayer(Player):
    def make_a_move(self):
        position = round(random.uniform(0, 1))
        return super().make_a_move(position)
