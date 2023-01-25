'''
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected_output = 6
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example2(self):
        nums = [1]
        expected_output = 1
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example3(self):
        nums = [5,4,-1,7,8]
        expected_output = 23
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

    def test_all_negative(self):
        nums = [-5, -10, -15, -20]
        expected_output = -5
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

#############################
if __name__ == '__main__':
    unittest.main()