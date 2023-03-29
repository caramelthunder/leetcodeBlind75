import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_263_solution import Solution

class Tes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 6
        expected_output = True

        actual_output = self.solution.isUgly(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        n = 1
        expected_output = True

        actual_output = self.solution.isUgly(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        n = 14
        expected_output = False

        actual_output = self.solution.isUgly(n)
        self.assertEqual(actual_output, expected_output)
    
######################################
if __name__ == '__main__':
    unittest.main()