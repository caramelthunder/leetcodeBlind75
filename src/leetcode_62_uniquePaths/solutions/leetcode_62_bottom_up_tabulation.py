
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]

'''
Example 1:

    |A|| || || || || || |
    | || || || || || || |
    | || || || || || ||Z|

Input: m = 3, n = 7
Output: 28
'''

