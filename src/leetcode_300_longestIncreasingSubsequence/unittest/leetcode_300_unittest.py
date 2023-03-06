import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_300_top_down_memoisation import Solution as Solution1
from solutions.leetcode_300_bottom_up_tabulation import Solution as Solution2
from solutions.leetcode_300_binary_search import Solution as Solution3

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
    
    def test_example_1(self):
        nums = [10,9,2,5,3,7,101,18]
        expected_output = 4

        actual_output = self.solution1.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [0,1,0,3,2,3]
        expected_output = 4

        actual_output = self.solution1.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        nums = [7,7,7,7,7,7,7]
        expected_output = 1

        actual_output = self.solution1.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        nums = [5,46,85,26,1,5,78,45,122,56,47,26]
        expected_output = 4

        actual_output = self.solution1.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.lengthOfLIS(nums)
        self.assertEqual(actual_output, expected_output)
######################################
if __name__ == '__main__':
    unittest.main()