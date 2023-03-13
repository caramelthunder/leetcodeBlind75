import math

class Solution:
    def numSquares(self, n: int):
        return self._numSquares(n, {})
    
    def _numSquares(self, n, cache):
        if n == 0:
            return 0
        
        sqrt_n = math.sqrt(n)

        if n not in cache:
            candidate = float('inf')

            for num in range(int(sqrt_n), 0, -1):
                perfect_square = num * num
                candidate = min(candidate, self._numSquares(n - perfect_square, cache) + 1)
                
            cache[n] = candidate

        return cache[n]