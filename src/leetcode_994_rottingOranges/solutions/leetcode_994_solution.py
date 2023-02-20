from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        minute = 0
        rotten_oranges = deque([])
        fresh_oranges = 0

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col, minute))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        while rotten_oranges:
            row, col, minute = rotten_oranges.popleft()

            for _r, _c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row = _r + row
                new_col = _c + col
                if R > new_row >= 0 and C > new_col >= 0 and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append((new_row, new_col, minute + 1))
                
        return minute if fresh_oranges == 0 else -1