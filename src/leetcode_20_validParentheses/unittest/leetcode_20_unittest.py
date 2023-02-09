import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_20_solution import Solution
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
        input_string = "{[()]}"
        expected_output = True

        output = self.s.main(input_string)
        self.assertEqual(output, expected_output)
        
    def test_unbalanced_parentheses_with_other_characters(self):
        input_string = "{[()]f"
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


