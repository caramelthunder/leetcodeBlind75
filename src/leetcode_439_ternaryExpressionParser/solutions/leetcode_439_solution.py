class Solution:
    def parseTernary(self, expression: str) -> str:
        """
        Evaluates a given ternary expression string and returns its result.

        Args:
            expression (str): The ternary expression string.

        Returns:
            str: The result of the ternary expression.
        """
        stack = []

        for char in reversed(expression):
            if stack and stack[-1] == "?":
                stack.pop()  # Popping '?'
                onTrue, onFalse = stack.pop(), stack.pop()
                stack.append(onTrue if char == "T" else onFalse)
            elif char != ":":
                stack.append(char)

        # If the expression is properly formatted,
        # we should only have one result in the stack.
        return stack[0] if len(stack) == 1 else None
