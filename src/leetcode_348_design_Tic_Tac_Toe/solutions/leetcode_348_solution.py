class TicTacToe:
    """
    A class to represent a TicTacToe game.

    Attributes:
    n (int): The size of the board.
    winning_rows (List[List[int, int]]): Tracks the score and previous player for each row.
    winning_cols (List[List[int, int]]): Tracks the score and previous player for each column.
    winning_diagonal (List[int, int]): Tracks the score and previous player for the main diagonal.
    winning_anti_diagonal (List[int, int]): Tracks the score and previous player for the anti-diagonal.
    """

    def __init__(self, n: int):
        self.n = n
        self.winning_rows = [[0, None] for _ in range(n)]
        self.winning_cols = [[0, None] for _ in range(n)]
        self.winning_diagonal = [0, None]
        self.winning_anti_diagonal = [0, None]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Makes a move on the board.

        Parameters:
        row (int): The row index of the move.
        col (int): The column index of the move.
        player (int): The player making the move (1 or 2).

        Returns:
        int: The player number if they won with this move, 0 otherwise.

        Time Complexity:
        O(1) - All operations (updating rows, columns, diagonals, and checking for a win) are constant time.

        Space Complexity:
        O(1) - We're using a constant amount of space regardless of the board size.
        """
        row_completed = (
            col_completed
        ) = diag_completed = anti_diag_completed = False

        row_completed = self._evaluate(self.winning_rows[row], player)
        col_completed = self._evaluate(self.winning_cols[col], player)
        if row == col:
            diag_completed = self._evaluate(self.winning_diagonal, player)
        if row + col == self.n - 1:
            anti_diag_completed = self._evaluate(
                self.winning_anti_diagonal, player
            )

        if (
            row_completed
            or col_completed
            or diag_completed
            or anti_diag_completed
        ):
            return player

        return 0

    def _evaluate(self, curr, player) -> bool:
        score, prev_player = curr
        score += (player == prev_player) or (prev_player is None)
        curr[0] = score
        curr[1] = player
        return score == self.n
