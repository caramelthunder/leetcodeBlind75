import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_556_solution import Solution 

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 12
        expected_output = 21

        actual_output = self.solution.nextGreaterElement(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        n = 21
        expected_output = -1

        actual_output = self.solution.nextGreaterElement(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        n = 12543
        expected_output = 13245

        actual_output = self.solution.nextGreaterElement(n)
        self.assertEqual(actual_output, expected_output)
    


######################################
if __name__ == '__main__':
    unittest.main()