class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        for row in range(R):
            for col in range(C):
                if self._dfs(board, R, C, word, 0, row, col, set()):
                    return True
        return False

    def _dfs(self, board, R, C, word, i, row, col, visited):
        if i >= len(word):
            return True
        
        if not (R > row >= 0 and C > col >= 0) \
            or (row, col) in visited \
            or board[row][col] != word[i]: return False
        
        visited.add((row, col))

        for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r = _r + row
            next_c = _c + col
            
            if self._dfs(board, R, C, word, i + 1, next_r, next_c, visited):
                return True
            
        visited.remove((row, col))
        return False
