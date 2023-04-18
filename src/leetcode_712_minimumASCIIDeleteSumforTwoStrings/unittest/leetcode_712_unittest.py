import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_712_memoisation import Solution as Solution1
from solutions.leetcode_712_tabulation import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "s1": "sea",
            "s2": "eat"
        }
        expected_output = 231

        actual_output = self.sol1.minimumDeleteSum(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minimumDeleteSum(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            "s1": "delete",
            "s2": "leet"
        }
        expected_output = 403

        actual_output = self.sol1.minimumDeleteSum(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minimumDeleteSum(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = {
            "s1": "abbbccbcbcbdjewb",
            "s2": "zxyyzxy"
        }
        expected_output = 2452

        actual_output = self.sol1.minimumDeleteSum(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minimumDeleteSum(**params)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()