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
        self.__check_winner()

    def __show_winner(self):
        if (self._winner_status == 1) | (self._winner_status == 2):
            print(f'The winner is {WINNER_STATUS.get(self._winner_status)}')
        elif self._winner_status == 3:
            print('No winner in this game... :(')

    def __check_if_filled(self):
        return '-' not in self._board

    def __check_winner(self):
        """Check if in each row, column or diagonal there is a winner
        """
        for i in range(self._length):
            if self._board[i, 0] == self._board[i, 1] == self._board[i, 2]:
                self._winner_status = self._board[i, 0]
                return True

        # check columns
        for i in range(self._length):
            if self._board[0, i] == self._board[1, i] == self._board[2, i]:
                self._winner_status = self._board[0, i]
                return True

        # check diagonals
        if self._board[0, 0] == self._board[1, 1] == self._board[2, 2]:
            self._winner_status = self._board[0, 0]
            return True

        if self._board[0, 2] == self._board[1, 1] == self._board[2, 0]:
            self._winner_status = self._board[0, 2]
            return True

        return False

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
