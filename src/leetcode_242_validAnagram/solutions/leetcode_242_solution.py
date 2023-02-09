from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = Counter(s)
        
        for char in t:
            if char in s_chars:
                s_chars[char] -= 1
                if s_chars[char] == 0:
                    del s_chars[char]
            else:
                return False

        return len(s_chars) == 0