import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_8_solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "42"
        expected_output = 42

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        s = "   -42"
        expected_output = -42

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        s = "4193 with words"
        expected_output = 4193

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        s = "words and 987"
        expected_output = 0

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_5(self):
        s = "3.14159"
        expected_output = 3

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_6(self):
        s = "+123"
        expected_output = 123

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_7(self):
        s = "+-345"
        expected_output = 0

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_8(self):
        s = "-+345"
        expected_output = 0

        actual_output = self.solution.myAtoi(s)
        self.assertEqual(actual_output, expected_output)

    

######################################
if __name__ == '__main__':
    unittest.main()