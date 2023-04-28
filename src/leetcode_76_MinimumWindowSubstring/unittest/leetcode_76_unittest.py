import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_76_solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        params = {
            's': "ADOBECODEBANC",
            't': "ABC"
        }
        expected_output = "BANC"

        actual_output = self.sol.minWindow(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            's': "a",
            't': "a"
        }
        expected_output = "a"

        actual_output = self.sol.minWindow(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = {
            's': "a",
            't': "aa"
        }
        expected_output = ""

        actual_output = self.sol.minWindow(**params)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()