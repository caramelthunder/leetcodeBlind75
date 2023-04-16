class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        # initialize the dp table with zeros
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]

        # fill in the dp table bottom-up
        for i2 in range(n2 - 1, -1, -1):
            for i1 in range(n1 - 1, -1, -1):
                # if the characters at the current positions are the same, add one to the LCS
                if text1[i1] == text2[i2]:
                    dp[i2][i1] = 1 + dp[i2 + 1][i1 + 1]
                # otherwise, take the max of skipping one character in s1 or s2
                else:
                    dp[i2][i1] = max(
                        dp[i2][i1 + 1],
                        dp[i2 + 1][i1]
                    )

        # return the result
        return dp[0][0]

# Time complexity analysis:
# The dp table has (m+1)*(n+1) entries, and each entry requires constant amount of work.
# Therefore, the total number of computations is O(m*n), where m and n are the lengths of the input strings.
# This is much faster than the recursive approach with memoization.
# However, the space complexity is larger because we need to store the entire dp table,
# which has (m+1)*(n+1) entries and requires O(m*n) space.

# Space complexity analysis:
# The dp table has (m+1)*(n+1) entries, each of which requires constant amount of space.
# Therefore, the space complexity is O(m*n).
