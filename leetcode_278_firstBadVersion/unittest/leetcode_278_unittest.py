import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_278_solution import Solution

class Test(unittest.TestCase):
    def test_example_1(self):
        versions = [False, False, False, True, True]
        n = 5
        expected_output = 4
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        versions = [False, False, False, True, True, True, True, True, True, True, True]
        n = 11
        expected_output = 4
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_last_value(self):
        versions = [False, False, False, False, False, False, True]
        n = 7
        expected_output = 7
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_first_value(self):
        versions = [True, True, True]
        n = 3
        expected_output = 1
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)

################################################
if __name__ == '__main__':
    unittest.main()
