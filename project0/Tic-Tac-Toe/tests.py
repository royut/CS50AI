from tictactoe import *

user = None
board = initial_state()
ai_turn = False


if __name__ == "__main__":
    print("running tests...")
    print("check taken move")
    try:
        board = result(board, (0, 0))
        print(board)
        board = result(board, (0, 0))
        print(board)
    except:
        print("test 1 passed")
    board = initial_state()
    print("check negative move")
    try:
        board = result(board, (-1, -1))
    except:
        print("test 2 passed")
