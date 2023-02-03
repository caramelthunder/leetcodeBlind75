import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_704_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [-1,0,3,5,9,12]
        target = 9
        expected_output = 4
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_example2(self):
        nums = [-1,0,3,5,9,12]
        target = 2
        expected_output = -1
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
    
    def test_all_equal_target(self):
        nums = [5,5,5,5,5,5,5]
        target = 5
        expected_output = 3
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
    
    def test_all_not_equal_target(self):
        nums = [5,5,5,5,5,5,5]
        target = 4
        expected_output = -1
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_array(self):
        nums = []
        target = 9
        expected_output = -1
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_single_element_array(self):
        nums = [9]
        target = 9
        expected_output = 0
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_first_element(self):
        nums = [9,10,11,12,13]
        target = 9
        expected_output = 0
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_last_element(self):
        nums = [9,10,11,12,13]
        target = 13
        expected_output = 4
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_target_less_than_first_element(self):
        nums = [9,10,11,12,13]
        target = 8
        expected_output = -1
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_target_more_than_last_element(self):
        nums = [9,10,11,12,13]
        target = 14
        expected_output = -1
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)
        
    def test_two_element_array(self):
        nums = [9,10]
        target = 10
        expected_output = 1
        actual_output = self.solution.search(nums= nums, target= target)
        self.assertEqual(actual_output, expected_output)

##########################################\
if __name__ == '__main__':
    unittest.main()