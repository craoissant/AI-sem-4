def print_solution(board):
    """
    Print the solution board.
    """
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col, n):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True


def solve_n_queens(board, row, n):
    """
    Solve the N-Queens problem using backtracking.
    """
    if row == n:
        print_solution(board)  # Print the solution when all queens are placed
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            res = solve_n_queens(board, row + 1, n) or res

            # Backtrack
            board[row][col] = 0

    return res


def n_queens(n):
    """
    Solve the N-Queens problem for a board of size n x n.
    """
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")
    else:
        print("Solutions are shown above.")


# Example usage
n = 4  # Change this to any number of queens
n_queens(n)
