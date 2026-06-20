import math

# Define the players
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'
EMPTY_CELL = '_'

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board to the console.
    """
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_moves_left(board):
    """
    Checks if there are any empty cells remaining on the board.
    Returns True if moves are left, otherwise False.
    """
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY_CELL:
                return True
    return False

def evaluate(board):
    """
    Evaluates the board to check for a win state.
    Returns +10 if AI wins, -10 if Human wins, 0 for a draw or incomplete game.
    """
    # Check rows for a victory
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == AI_PLAYER:
                return 10
            elif board[row][0] == HUMAN_PLAYER:
                return -10

    # Check columns for a victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == AI_PLAYER:
                return 10
            elif board[0][col] == HUMAN_PLAYER:
                return -10

    # Check diagonals for a victory
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == AI_PLAYER:
            return 10
        elif board[0][0] == HUMAN_PLAYER:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == AI_PLAYER:
            return 10
        elif board[0][2] == HUMAN_PLAYER:
            return -10

    # No winner yet or game is a draw
    return 0

def minimax(board, depth, is_maximizing):
    """
    The Minimax recursive function. 
    Explores all possible moves to determine the optimal score.
    """
    score = evaluate(board)

    # Base cases: return score if terminal state is reached
    if score == 10:
        return score - depth # Subtract depth to prefer faster wins
    if score == -10:
        return score + depth # Add depth to prefer slower losses
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_val = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY_CELL:
                    # Make a tentative move
                    board[row][col] = AI_PLAYER
                    # Call minimax recursively
                    value = minimax(board, depth + 1, False)
                    best_val = max(best_val, value)
                    # Undo the move
                    board[row][col] = EMPTY_CELL
        return best_val
    else:
        best_val = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY_CELL:
                    # Make a tentative move
                    board[row][col] = HUMAN_PLAYER
                    # Call minimax recursively
                    value = minimax(board, depth + 1, True)
                    best_val = min(best_val, value)
                    # Undo the move
                    board[row][col] = EMPTY_CELL
        return best_val

def find_best_move(board):
    """
    Iterates through all empty cells to find the best move for the AI.
    Returns the coordinates (row, col) of the optimal move.
    """
    best_val = -math.inf
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY_CELL:
                # Make a tentative move
                board[row][col] = AI_PLAYER
                # Evaluate this move using minimax
                move_val = minimax(board, 0, False)
                # Undo the move
                board[row][col] = EMPTY_CELL

                # Update best move if current move is better
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val

    return best_move

def main():
    """
    Main execution loop to play the game in the terminal.
    """
    # Initialize an empty 3x3 board
    board = [
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
    ]

    print("Tic-Tac-Toe: Human (O) vs AI (X)")
    print_board(board)

    while is_moves_left(board):
        # Human turn
        print("\nYour turn.")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if row not in range(3) or col not in range(3) or board[row][col] != EMPTY_CELL:
            print("Invalid move. Cell is either out of bounds or already occupied.")
            continue

        board[row][col] = HUMAN_PLAYER
        print_board(board)

        if evaluate(board) == -10:
            print("You win! (This should be impossible against Minimax)")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI turn
        print("\nAI is calculating its move...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = AI_PLAYER
        print(f"AI plays at row {ai_row}, column {ai_col}")
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()