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


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Found a solution, append it to the list of solutions
        solutions.append(["".join([" Q" if cell == 1 else " *" for cell in row]) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen if it's safe
            board[row][col] = 1

            # Move to the next row
            solve_n_queens_util(board, row + 1, n, solutions)

            # Backtrack: Remove the queen if no solution found
            board[row][col] = 0


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


# Example :
n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-queens problem: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()









