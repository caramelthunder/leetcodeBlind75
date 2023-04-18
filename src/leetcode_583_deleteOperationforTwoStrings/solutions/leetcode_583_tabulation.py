class Solution:
    '''
    Let M be the length of string word1 and N be the length of string word2.

    Time Complexity: O(M * N)
    In the nested for-loop, the outer loop iterates M times, 
    and the inner loop iterates N times.

    Space Complexity: O(M * N)
    The space is for the additional 2-dimensional array dp of size (M * N)).
    '''

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        
        # create a 2D array for dynamic programming
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        
        # set base cases for when one of the words is empty
        for r in range(1, len(dp)):
            dp[r][0] = r
        for l in range(1, len(dp[-1])):
            dp[0][l] = l
        
        # fill the rest of the array with the minimum edit distance
        for i2 in range(1, len(dp)):
            for i1 in range(1, len(dp[0])):
                char1, char2 = word1[i1 - 1], word2[i2 - 1]

                # If the characters at the current indices match.
                if char1 == char2:
                    dp[i2][i1] = dp[i2 - 1][i1 - 1]
                else:
                    dp[i2][i1] = 1 + min(
                        # Delete char into word2.
                        dp[i2][i1 - 1],
                        # Delete char from word1.
                        dp[i2 - 1][i1]
                    )
        
        # return the minimum edit distance
        return dp[-1][-1]