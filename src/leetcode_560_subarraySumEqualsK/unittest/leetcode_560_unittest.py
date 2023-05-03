import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_560_solution import Solution as Solution1

class Test(unittest.TestCase):

    def setUp(self):
        self.sol = Solution1()

    def test_example_1(self):
        params = {
            'nums': [1,1,1],
            'k': 2
        }
        expected_output = 2

        actual_output = self.sol.subarraySum(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            'nums': [1,2,3],
            'k': 3
        }
        expected_output = 2

        actual_output = self.sol.subarraySum(**params)
        self.assertEqual(actual_output, expected_output)




######################################
if __name__ == '__main__':
    unittest.main()