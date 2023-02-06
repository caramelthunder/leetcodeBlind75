import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_15_using_sort import Solution as Solution1
from solutions.leetcode_15_using_hash_set_table import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        nums = [-1,0,1,2,-1,-4]
        expected_output = [[-1,-1,2],[-1,0,1]]
        
        actual_output1 = self.solution1.threeSum(nums)
        self.assertCountEqual(actual_output1, expected_output)

        actual_output2 = self.solution2.threeSum(nums)
        self.assertCountEqual(actual_output2, expected_output)

    def test_example_2(self):
        nums = [0,1,1]
        expected_output = []

        actual_output1 = self.solution1.threeSum(nums)
        self.assertCountEqual(actual_output1, expected_output)

        actual_output2 = self.solution2.threeSum(nums)
        self.assertCountEqual(actual_output2, expected_output)

    def test_example_3(self):
        nums = [0,0,0]
        expected_output = [[0,0,0]]
        
        actual_output1 = self.solution1.threeSum(nums)
        self.assertCountEqual(actual_output1, expected_output)

        actual_output2 = self.solution2.threeSum(nums)
        self.assertCountEqual(actual_output2, expected_output)
    
    def test_example_4(self):
        nums = [1,-1,2,1]
        expected_output = []

        actual_output1 = self.solution1.threeSum(nums)
        self.assertCountEqual(actual_output1, expected_output)

        actual_output2 = self.solution2.threeSum(nums)
        self.assertCountEqual(actual_output2, expected_output)

#####################################
if __name__ == '__main__':
    unittest.main()