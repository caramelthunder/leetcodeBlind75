import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_202_using_hashSet import Solution as Solution1
from solutions.leetcode_202_slow_fast_recursive import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "n": 19
        }
        expected_output = True

        actual_output = self.sol1.isHappy(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.isHappy(**params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        params = {
            "n": 2
        }
        expected_output = False

        actual_output = self.sol1.isHappy(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.isHappy(**params)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()