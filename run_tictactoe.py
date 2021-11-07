from tictactoe import TicTacToe

tictacttoe_game = TicTacToe()
print(tictacttoe_game)
tictacttoe_game.show_board()
for turn in tictacttoe_game:
    tictacttoe_game.show_board()

tictacttoe_game.show_winner()
