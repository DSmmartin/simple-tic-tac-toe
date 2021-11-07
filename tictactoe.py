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

    def __iter__(self):
        return self

    def __next__(self):
        if self._winner_status == 0:
            self.__run_cycle()
            self._iteration += 1
            if self.__check_if_filled():
                self._winner_status = 3
        else:
            raise StopIteration

    def show_board(self):
        print(f'-- Board at iteration: {self._iteration}')
        print(self._board)  # TODO: improve visualization

    def __run_cycle(self):
        self.__check_winner()

    def show_winner(self):
        if (self._winner_status == 1) | (self._winner_status == 2):
            print(f'The winner is {WINNER_STATUS.get(self._winner_status)}')
        elif self._winner_status == 3:
            print('No winner in this game... :(')

        else:
            print('Something went wrong...')

    def __check_if_filled(self):
        return '-' not in self._board

    def __check_winner(self):
        """Check if in each row, column or diagonal there is a winner
        """
        # check rows
        for i in range(self._length):
            if ('-' not in self._board[i, :]) and (self._board[i, :] == self._board[i, 0]):
                self._winner_status = self._board[i, 0]
                return True

        # check columns
        for i in range(self._length):
            if ('-' not in self._board[:, i]) and (self._board[0, i] == self._board[0, i]):
                self._winner_status = self._board[0, i]
                return True

        # check diagonals
        board_diag = np.diag(self._board)
        if ('-' not in board_diag) and (board_diag == board_diag[0]):
            self._winner_status = board_diag[0]
            return True

        # obtain inverse diagonal of board
        board_diag_inv = np.diag(np.fliplr(self._board))
        if ('-' not in board_diag_inv) and (board_diag_inv == board_diag_inv[0]):
            self._winner_status = board_diag_inv[0]
            return True

        return False

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
