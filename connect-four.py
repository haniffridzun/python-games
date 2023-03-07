import numpy as np

ROW_COUNT = 6
COL_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_loc(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # check horizontal location for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # check vertical location for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # check positive slope
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # check negative slope
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
game_over = False
turn = 0
print_board(board)

while not game_over:
    # ask player1 input
    if turn == 0:
        col = int(input("player 1 make selection (0-6):"))
        if is_valid_loc(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            # winning condition
            if winning_move(board, 1):
                print('player 1 wins!')
                game_over = True
                break
    # ask player2 input
    else:
        col = int(input("player 2 make selection (0-6):"))
        if is_valid_loc(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            # winning condition
            if winning_move(board, 2):
                print('player 2 wins!')
                game_over = True
                break

    print_board(board)
    turn += 1
    turn = turn % 2
