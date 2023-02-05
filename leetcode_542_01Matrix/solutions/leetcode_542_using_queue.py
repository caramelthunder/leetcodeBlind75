from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        R, C = len(mat), len(mat[0])
        _mat = [[float('inf')] * C for _ in range(R)]
        q = deque([])

        for row in range(R):
            for col in range(C):
                if mat[row][col] == 0:
                    _mat[row][col] = mat[row][col]
                    q.append((row, col))
        
        while q:
            row, col = q.popleft()
            for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                adj_row, adj_col = _r + row, _c + col
                if R > adj_row >= 0 and C > adj_col >= 0: 
                    if _mat[adj_row][adj_col] > _mat[row][col] + 1:
                        _mat[adj_row][adj_col] = _mat[row][col] + 1
                        q.append((adj_row, adj_col))
                    
        return _mat