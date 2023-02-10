import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1_solution import Solution

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        input_nums = [2,7,11,15]
        target = 9
        expected_output = {0,1}

        output = set(self.s.twoSum(input_nums, target))
        self.assertEqual(output, expected_output)

    def test_example2(self):
        input_nums = [3,2,4]
        target = 6
        expected_output = {1,2}

        output = set(self.s.twoSum(input_nums, target))
        self.assertEqual(output, expected_output)
        
    def test_example3(self):
        input_nums = [3,3]
        target = 6
        expected_output = {0,1}

        output = set(self.s.twoSum(input_nums, target))
        self.assertEqual(output, expected_output)
        
    def test_different_order(self):
        input_nums = [2,7,11,15]
        target = 9
        expected_output = {1,0}

        output = set(self.s.twoSum(input_nums, target))
        self.assertEqual(output, expected_output)
        
    def test_not_found(self):
        input_nums = [1, 2, 3, 4, 5]
        target = 10
        expected_output = {-1, -1}

        output = set(self.s.twoSum(input_nums, target))
        self.assertEqual(output, expected_output)

###################################
if __name__ == '__main__':
    unittest.main()