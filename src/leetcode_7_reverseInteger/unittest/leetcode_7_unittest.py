import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_7_solution import Solution 

class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        x = 123
        expected_output = 321

        actual_output = self.sol.reverse(x=x)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        x = -123
        expected_output = -321

        actual_output = self.sol.reverse(x=x)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        x = 120
        expected_output = 21

        actual_output = self.sol.reverse(x=x)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        x = 1534236469
        expected_output = 0

        actual_output = self.sol.reverse(x=x)
        self.assertEqual(actual_output, expected_output)

    def test_example_5(self):
        x = -1463847412
        expected_output = -2147483641

        actual_output = self.sol.reverse(x=x)
        self.assertEqual(actual_output, expected_output)

    


######################################
if __name__ == '__main__':
    unittest.main()
'''
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''
