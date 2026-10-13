"""
Tic-Tac-Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns the player who has the next turn on a board.
    """
    countX, countO = 0, 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    return X if countX <= countO else O


def actions(board):
    """
    Returns the set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row_num in range(len(board)):
        for cell_num in range(len(board[row_num])):
            if board[row_num][cell_num] == EMPTY:
                possible_actions.add((row_num, cell_num))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making the move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid move")
    new_board = []
    for row in board:
        temp_row = []
        for cell in row:
            temp_row.append(cell)
        new_board.append(temp_row)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_action = None
    if player(board) == X:
        # we want highest utility
        v = float('-inf')
        for action in actions(board):
            temp = min_value(result(board, action))
            if temp > v:
                v = temp
                best_action = action
    elif player(board) == O:
        # we want lowest utility
        v = float('inf')
        best_action = None
        for action in actions(board):
            temp = max_value(result(board, action))
            if temp < v:
                v = temp
                best_action = action
    return best_action


def max_value(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
