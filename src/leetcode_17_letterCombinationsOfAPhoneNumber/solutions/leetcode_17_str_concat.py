class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        lookup = {
            '1': '', '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        return self._letterCombinations(digits, lookup)
    
    def _letterCombinations(self, digits, lookup):
        if not digits:
            return [""]
        
        digit = digits[0]
        chars = lookup[digit]

        comb_without_chars = self._letterCombinations(digits[1:], lookup)
        comb_with_chars = []

        for char in chars:
            for comb in comb_without_chars:
                comb_with_chars.append(char + comb)

        return comb_with_chars

        