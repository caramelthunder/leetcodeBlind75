from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        island_count = 0

        for row in range(R):
            for col in range(C):
                if grid[row][col] == '1':
                    island_count += 1
                    self._numIslands(grid, R, C, row, col)
        return island_count

    def _numIslands(self, grid, R, C, row, col):
        q = deque([(row, col)])
        grid[row][col] = '0'

        while q:
            row, col = q.popleft()

            for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = _r + row
                new_col = _c + col
                if R > new_row >= 0 and C > new_col >= 0 and grid[new_row][new_col] == '1':
                    grid[new_row][new_col]  = '0'
                    q.append((new_row, new_col))