'''
LC_001 "https://leetcode.com/problems/two-sum/"

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        char_map = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            
            if comp in char_map:
                return [char_map[comp], i]
            char_map[num] = i
            
        return [-1, -1]
    
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