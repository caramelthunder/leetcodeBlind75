class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        lookup = {
            '1': '', '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        output = []
        self._letterCombinations(digits, 0, lookup, "", output)
        return output
    
    def _letterCombinations(self, digits, i, lookup, curr, output):
        
        if len(curr) == len(digits):
            output.append(curr)
            return 

        digit = digits[i]
        for char in lookup[digit]:
            self._letterCombinations(digits, i + 1, lookup, curr + char, output)