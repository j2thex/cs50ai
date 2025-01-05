"""
Tic Tac Toe Player
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
    Returns player who has the next turn on a board.
    This function needs to determine whose turn it is (X or O)
X always goes first in the initial state
Players alternate turns
You can determine whose turn it is by counting the number of X's and O's on the board
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # Check for negative indices or out of bounds moves
    if not (0 <= i <= 2 and 0 <= j <= 2):
        raise ValueError("Invalid action: move out of bounds")

    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    # Manual deep copy of the board
    new_board = [[board[i][j] for j in range(3)] for i in range(3)]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
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
    if terminal(board):
        return None

    current_player = player(board)
    
    if current_player == X:
        best_value = float('-inf')
        best_move = None
        
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = float('inf')
        best_move = None
        
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
                
    return best_move


def max_value(board):
    """
    Helper function for minimax that maximizes the value
    """
    if terminal(board):
        return utility(board)
        
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Helper function for minimax that minimizes the value
    """
    if terminal(board):
        return utility(board)
        
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
    