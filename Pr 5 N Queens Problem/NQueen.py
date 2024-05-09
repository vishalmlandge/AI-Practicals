def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


# Used to solve the N Queen Problem
def solve_n_queens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            # If the condition is true, place Queen
            board[row][col] = 1
            print_board(board)

            if solve_n_queens_util(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main function that starts the process
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()


# Example :
n = 4
print(f"Solving {n}-queens problem:")
solve_n_queens(n)
