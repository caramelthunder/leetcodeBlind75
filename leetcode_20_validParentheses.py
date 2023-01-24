'''
Leetcode 20 "https://leetcode.com/problems/valid-parentheses/"

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

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

import unittest 
class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_valid_parentheses(self):
        input_string = "()[]{}"
        expected_output = True

        output = self.s.main(input_string)
        self.assertEqual(output, expected_output)

    def test_invalid_parentheses(self):
        input_string = "(]"
        expected_output = False

        output = self.s.main(input_string)
        self.assertEqual(output, expected_output)

    def test_balanced_parentheses_with_other_characters(self):
        input_string = "a{b[c(d)e]f}g"
        expected_output = True

        output = self.s.main(input_string)
        self.assertEqual(output, expected_output)
        
    def test_unbalanced_parentheses_with_other_characters(self):
        input_string = "a{b[c(d)e]f"
        expected_output = False

        output = self.s.main(input_string)
        self.assertEqual(output, expected_output)
        
    def test_empty_string(self):
        input_string = ""
        expected_output = True

        output = self.s.main(input_string)
        self.assertEqual(output, expected_output)

##################################
if __name__ == '__main__':
    unittest.main()


