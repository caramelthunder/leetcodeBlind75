import math

class Solution:
    def numSquares(self, n: int):
        sqrt_n = math.sqrt(n)

        if sqrt_n == int(sqrt_n):
            return 1

        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, int(sqrt_n) + 1):
            perfect_square = i * i
            for num in range(perfect_square, n + 1):
                dp[num] = min(dp[num], dp[num - perfect_square] + 1)
        
        return dp[n]