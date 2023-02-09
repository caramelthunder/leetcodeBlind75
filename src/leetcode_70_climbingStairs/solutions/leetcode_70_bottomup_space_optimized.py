class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self._climbStairs(n, cache)
    
    def _climbStairs(self, n, cache):
        if n == 0 or n == 1:
            return 1

        if n not in cache:
            cache[n] = self._climbStairs(n - 1, cache) + self._climbStairs(n - 2, cache) 
        return cache[n]