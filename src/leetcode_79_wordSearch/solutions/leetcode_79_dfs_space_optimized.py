class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        for row in range(R):
            for col in range(C):
                attempt = self._dfs(board, word, R, C, row, col)
                if attempt:
                    return True
        return False

    def _dfs(self, board, word, R, C, row, col):
        if word == "":
            return True
        
        if not (R > row >= 0 and C > col >= 0) or \
            board[row][col] == "visited" or \
            board[row][col] != word[0]: return False
            
        saved_val = board[row][col]
        board[row][col] = "visited"

        for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row = _r + row
            next_col = _c + col

            if self._dfs(board, word[1:], R, C, next_row, next_col):
                return True
        
        board[row][col] = saved_val
        return False


