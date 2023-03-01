class Solution:
    def wordBreak(self,s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}
        return self._wordBreak(s, wordDict, cache)

    def _wordBreak(self, word, wordDict, cache):
        if word == "" or word in wordDict:
            return True
        
        if word not in cache:

            for i in range(len(word) + 1):
                prefix = word[:i]
                if prefix in wordDict:
                    suffix = word[i:]
                    if self._wordBreak(suffix, wordDict, cache):
                        cache[word] = True
                        return True

        cache[word] = False
        return False