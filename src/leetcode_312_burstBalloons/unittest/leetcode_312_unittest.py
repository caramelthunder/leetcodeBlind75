import sys
import os
import unittest
import copy

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_312_naive import Solution as Solution1
from solutions.leetcode_312_top_down_memoisation import Solution as Solution2
from solutions.leetcode_312_bottom_up_tabulation import Solution as Solution3

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
    
    def test_example_1(self):
        nums = [3,1,5,8]
        expected_output = 167

        actual_output = self.solution1.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [1,5,4]
        expected_output = 30

        actual_output = self.solution1.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = [1,5]
        expected_output = 10

        actual_output = self.solution1.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        nums = [23,10,398,209,239,293,348,120,348,457,10,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
        39,457,50,10,80,28,10,387,165,235,218,98]
        expected_output = 481421654

        # actual_output = self.solution1.maxCoins(copy.deepcopy(nums))
        # self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.maxCoins(copy.deepcopy(nums))
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()