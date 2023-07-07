class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluates an arithmetic expression with parentheses and positive and negative integers.

        Args:
            s (str): A string representing an arithmetic expression. The expression may contain digits, parentheses,
                     plus and minus signs, and spaces. The parentheses must be well-formed.

        Returns:
            int: The result of evaluating the arithmetic expression.

        Raises:
            ValueError: If the input string contains invalid characters or the parentheses are not well-formed.
        """

        s = s.replace(" ", "")
        stack = []
        bracket_stack = []
        sign_stack = []

        i = 0
        while i < len(s):
            char = s[i]
            if char == "(":
                stack.append(0)
                bracket_stack.append(len(stack))
                sign_stack.append("-" if i > 0 and s[i - 1] == "-" else "+")
            elif char == ")":
                while len(stack) > bracket_stack[-1]:
                    stack.append(stack.pop() + stack.pop())
                bracket_stack.pop()
                stack[-1] = (
                    -stack[-1] if sign_stack.pop() == "-" else stack[-1]
                )
            elif char.isdigit():
                sign = "-" if i > 0 and s[i - 1] == "-" else "+"
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(-int(num) if sign == "-" else int(num))
                i -= 1
            i += 1

        if bracket_stack:
            return None
        return sum(stack)
