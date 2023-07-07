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
        # used to store intermediate results and signs when processing nested parentheses
        stack = []
        num = 0  # used to accumulate the digits of a number
        sign = 1  # the sign of the current number
        res = 0  # the current result
        _prev_char = None  # the previous non-space character

        for char in s:
            if char == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1

            elif char.isdigit():
                num = num * 10 + int(char)  # accumulate the digits of a number

            elif char == "+":
                if not _prev_char or _prev_char in ["+", "-", "("]:
                    raise ValueError(f"Invalid input string: {s}")
                res += sign * num
                num, sign = 0, 1

            elif char == "-":
                res += sign * num
                num = 0
                # handle consecutive minus signs
                sign = 1 if _prev_char and _prev_char == "-" else -1

            elif char == ")":
                res += sign * num
                # apply the sign before the opening parenthesis
                res *= stack.pop()
                # add the result before the opening parenthesis
                res += stack.pop()
                num, sign = 0, 1

            if char != " ":
                _prev_char = char

        return res + sign * num
