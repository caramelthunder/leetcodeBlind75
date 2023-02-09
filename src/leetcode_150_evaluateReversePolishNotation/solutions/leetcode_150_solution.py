import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y)
        }

        stack = []
        for val in tokens:
            if val in operations:
                operator = val
                if stack:
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(operations[operator](x, y))
            else:
                stack.append(int(val))

        return stack[-1] if stack else 0