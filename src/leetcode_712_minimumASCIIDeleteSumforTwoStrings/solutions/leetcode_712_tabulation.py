class Solution:
    '''
    Time Complexity: O(M * N), where M,N are the lengths of the given strings. 
    We use nested for loops: each loop is O(M) and O(N) respectively.

    Space Complexity: O(M * N), the space used by 2-D dp array.
    '''

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
    
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for i2, char2 in enumerate(s2):
            dp[i2 + 1][0] = dp[i2][0] + ord(char2)
        for i1, char1 in enumerate(s1):
            dp[0][i1 + 1] = dp[0][i1] + ord(char1)
        
        for i2 in range(1, len(dp)):
            for i1 in range(1, len(dp[0])):
                char1, char2 = s1[i1 - 1], s2[i2 - 1]
                
                if char1 == char2:
                    dp[i2][i1] = dp[i2 - 1][i1 - 1]
                else:
                    dp[i2][i1] = min(
                        # Delete char from s1.
                        ord(char1) + dp[i2][i1 - 1],
                        # Delete char from s2.
                        ord(char2) + dp[i2 - 1][i1],
                    )
                        
        return dp[-1][-1]