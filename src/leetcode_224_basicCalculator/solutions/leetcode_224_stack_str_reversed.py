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

        def evaluate_expression(open_bracket_pos) -> int:
            # Calculate the sum of all elements in the stack
            # from the current position to the open_bracket_pos
            pos = len(stack)
            res = 0

            while pos > open_bracket_pos:
                res += stack.pop()
                pos -= 1
            return res

        stack = []  # Stack to store the numbers in the expression
        # Stack to store the positions of the opening brackets
        open_bracket_pos = []
        num_str = ""  # String to accumulate the digits of a number

        # Process the string in reverse order
        for char in s[::-1]:
            if char.isdigit():
                # If the character is a digit, add it to the left of the current number string
                num_str = char + num_str
            else:
                # If the character is not a digit,
                # convert the current number string to an integer and push it onto the stack
                if num_str != "":
                    stack.append(int(num_str))
                    num_str = ""

                if char == ")":
                    # If the character is a closing parenthesis,
                    # save the position of the top of the stack and push a zero onto the stack
                    open_bracket_pos.append(len(stack))
                    stack.append(0)
                elif char == "(":
                    # If the character is an opening parenthesis,
                    # evaluate the expression inside the parentheses and push the result onto the stack
                    stack.append(evaluate_expression(open_bracket_pos.pop()))
                elif char == "-":
                    # If the character is a minus sign, negate the top item of the stack
                    stack[-1] = -stack[-1]

        # If there's still a number string, convert it to an integer and push it onto the stack
        if num_str != "":
            stack.append(int(num_str))

        # Evaluate the entire expression and return the result
        return evaluate_expression(0)
