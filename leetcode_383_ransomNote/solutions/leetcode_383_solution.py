from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        magazine_map = Counter(magazine)

        for char in ransomNote:
            if magazine_map[char] == 0:
                return False
            magazine_map[char] -= 1

        return True