class Solution:
    '''
    Let M be the length of string word1 and N be the length of string word2.

    Time Complexity: O(M * N)
    As the memoization approach uses the cache, 
    for every combination of word1 and word2 the result is computed only once.

    Space Complexity: O(M * N)
    The space is for the additional hashmap cache of size (M * N).
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        
        # Call the helper function with initial indices and an empty cache dictionary
        return self._min_distance(word1, word2, 0, 0, {})
    
    def _min_distance(self, word1, word2, i1, i2, cache):
        # Base case: if either string is exhausted, return the remaining length of the other string
        if i1 >= len(word1):
            return len(word2) - i2
        if i2 >= len(word2):
            return len(word1) - i1
        
        # Check if the current indices are already in the cache
        key = (i1, i2)
        if key not in cache:
            # If the characters at the current indices match, move on to the next indices
            if word1[i1] == word2[i2]:
                cache[key] = self._min_distance(word1, word2, i1 + 1, i2 + 1, cache)
            else:
                # Otherwise, recursively compute the minimum distance using each of the two operations
                cache[key] = 1 + min(
                    # Delete char into word2.
                    self._min_distance(word1, word2, i1, i2 + 1, cache),
                    # Delete char from word1.
                    self._min_distance(word1, word2, i1 + 1, i2, cache),
                )
        
        # Return the result for the current indices
        return cache[key]