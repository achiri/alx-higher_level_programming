import sys

def nqueens(n):
    """Solves the N-queens problem.

    Args:
        n (int): The number of queens to place on the board.

    Returns:
        A list of integers representing the positions of the queens on the board.
    """

    board = [None] * n

    def place_queen(row, col):
        """Places a queen on the board at the given row and column.

        Args:
            row (int): The row to place the queen on.
            col (int): The column to place the queen on.
        """

        board[row] = col

    def is_valid_placement(row, col):
        """Checks to see if the queen can be placed on the board at the
        given row and column without attacking any other queens.

        Args:
            row (int): The row to place the queen on.
            col (int): The column to place the queen on.

        Returns:
            True if the placement is valid, False otherwise.
        """

        for i in range(row):
            if board[i] == col or abs(row - i) == abs(col - board[i]):
                return False

        return True

    def solve(row):
        """Recursively places queens on the board, one at a time.

        Args:
            row (int): The current row.

        Returns:
            True if a solution is found, False otherwise.
        """

        if row == n:
            return True

        for col in range(n):
            if is_valid_placement(row, col):
                place_queen(row, col)

                if solve(row + 1):
                    return True

                # Backtrack if no solution is found.
                board[row] = None

        return False

    if solve(0):
        return board
    else:
        return None

def main():
    n = int(sys.argv[1])

    solution = nqueens(n)

    if solution is not None:
        print("{} queens:".format(n))
        print(solution)
    else:
        print("No solution exists for {} queens.".format(n))

if __name__ == "__main__":
    main()
