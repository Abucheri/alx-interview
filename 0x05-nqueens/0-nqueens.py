#!/usr/bin/python3
"""
    The N queens puzzle is the challenge of placing N non-attacking
    queens on an N×N chessboard. This program solves the N queens problem.

    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line, and exit with the
        status 1.
    where N must be an integer greater or equal to 4:
        If N is not an integer, print N must be a number, followed by a new
        line, and exit with the status 1.
        If N is smaller than 4, print N must be at least 4, followed by a new
        line, and exit with the status 1.
    The program should print every possible solution to the problem:
        One solution per line.
        Format: see example.
        You don’t have to print the solutions in a specific order.
    You are only allowed to import the sys module.
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list of list): The chessboard.
        row (int): The current row.
        col (int): The current column.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row):
    """Solve the N queens problem using a recursive backtracking algorithm.

    Args:
        board (list of list): The chessboard.
        row (int): The current row.

    Returns:
        list of list: List of solutions.
    """
    # If reached the end of the board, return the current board configuration
    # as a solution
    if row == len(board):
        solution = ([[r, c] for r, row in enumerate(board)
                     for c, val in enumerate(row) if val == 1])
        return [solution]

    solutions = []
    # Try placing a queen in each column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1

            # Recur to next row
            sub_solutions = solve_nqueens(board, row + 1)

            # Add solutions found in the next row
            solutions.extend(sub_solutions)

            # Backtrack: remove the queen
            board[row][col] = 0

    return solutions


def print_solutions(solutions):
    """Print the solutions to the N queens problem.

    Args:
        solutions (list of list): List of solutions.
    """
    for solution in solutions:
        print(solution)


def main():
    """Main function"""
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the argument provided is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N Queens problem and print solutions
    solutions = solve_nqueens(board, 0)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
