class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # call the helper function with memoization
        return self._longestCommonSubsequence(text1, text2, 0, 0, {})

    def _longestCommonSubsequence(self, s1, s2, i1, i2, cache):
        # base case: one of the strings is empty, return zero
        if i1 == len(s1) or i2 == len(s2):
            return 0
        
        key = (i1, i2)
        if key not in cache:
            # if the characters at the current positions are the same, add one to the LCS
            if s1[i1] == s2[i2]:
                cache[key] = 1 + self._longestCommonSubsequence(s1, s2, i1 + 1, i2 + 1, cache)
            # otherwise, try skipping one character in s1 or s2 and take the max
            else:
                cache[key] = max(
                    self._longestCommonSubsequence(s1, s2, i1 + 1, i2, cache),
                    self._longestCommonSubsequence(s1, s2, i1, i2 + 1, cache)
                )

        return cache[key]

# Time complexity analysis:
# The function _longestCommonSubsequence is called recursively for each pair of characters in the input strings.
# The maximum number of recursive calls is m*n, where m and n are the lengths of the input strings.
# For each call, we do constant amount of work, which includes two recursive calls or one cache lookup,
# as well as a comparison and a conditional statement.
# Therefore, the time complexity is O(m*n) without memoization and O(m*n) with memoization.

# Space complexity analysis:
# The maximum depth of recursion is m+n, which means the maximum number of sets of arguments and local variables
# that exist at the same time is m+n. The size of each set of arguments and local variables is constant.
# In addition, we use a cache to store the results of previous computations, which has a maximum size of m*n.
# Therefore, the space complexity is O(m*n).
