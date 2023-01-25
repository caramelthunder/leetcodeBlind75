'''
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity. 

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

import unittest
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