import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_150_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2","1","+","3","*"]
        expected_output = 9
        actual_output = self.solution.evalRPN(tokens)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        tokens = ["4","13","5","/","+"]
        expected_output = 6
        actual_output = self.solution.evalRPN(tokens)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        expected_output = 22
        actual_output = self.solution.evalRPN(tokens)
        self.assertEqual(actual_output, expected_output)

##########################################
if __name__ == '__main__':
    unittest.main()
