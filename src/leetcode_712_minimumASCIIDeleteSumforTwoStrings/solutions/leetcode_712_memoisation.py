class Solution:
    '''
    Time Complexity: O(M * N), where M,N are the lengths of the given strings. 
    This is because the function does a recursive call for each pair of (i1, i2) values, 
    and there are M * N such pairs.

    Space Complexity: O(M * N), the space used by hashmap cache.
    '''
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        return self._minimumDeleteSum(s1, s2, 0, 0, {})
    
    def _minimumDeleteSum(self, s1, s2, i1, i2, cache):
        key = (i1, i2)

        if i1 == len(s1):
            cost_of_delete_remainder = 0
            for char in s2[i2: ]:
                cost_of_delete_remainder += ord(char)
            cache[key] = cost_of_delete_remainder
    
        if i2 == len(s2):
            cost_of_delete_remainder = 0
            for char in s1[i1: ]:
                cost_of_delete_remainder += ord(char)
            cache[key] = cost_of_delete_remainder
        
        if key not in cache:
            char1, char2 = s1[i1], s2[i2]
            
            if char1 == char2:
                cache[key] = self._minimumDeleteSum(s1, s2, i1 + 1, i2 + 1, cache)
            else:
                cache[key] = min(
                    # Delete char from s1.
                    ord(char1) + self._minimumDeleteSum(s1, s2, i1 + 1, i2, cache),
                    # Delete char from s2.
                    ord(char2) + self._minimumDeleteSum(s1, s2, i1, i2 + 1, cache)
                )
            
        return cache[key]