class Solution:
    def wordBreak(self,s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        dp = [True] + [False for _ in range(len(s))]

        for R in range(len(dp)):
            for L in range(R, -1, -1):
                if dp[L] is True:
                    prefix = s[L: R]
                    if prefix in wordDict:
                        dp[R] = True
                        break

        return dp[-1]