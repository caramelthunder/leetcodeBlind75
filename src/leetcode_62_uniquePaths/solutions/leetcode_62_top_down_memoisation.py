
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self._uniquePaths(m, n, {})
    
    def _uniquePaths(self, row, col, cache):
        if row == col == 1:
            return 1
        
        if row < 1 or col < 0:
            return 0

        key = (row, col)
        if key not in cache:
            paths = 0

            for _r, _c in [(-1, 0), (0, -1)]:
                new_row = _r + row
                new_col = _c + col
                paths += self._uniquePaths(new_row, new_col, cache)

            cache[key] = paths

        return cache[key]