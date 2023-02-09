class Solution:
    def main(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for bracket in s:
            if bracket in brackets:
                if not stack or brackets[bracket] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
                
        return len(stack) == 0
