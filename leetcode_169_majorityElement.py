'''
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_element = None
        count = 0

        for num in nums:
            if count == 0 or majority_element == num:
                majority_element = num
                count += 1
            elif majority_element != num:
                count -= 1

        return majority_element if count > 0 else None

        # # Boyer-Moore Majority Vote algorithm ##
        # for num in nums:
        #     if count == 0:
        #         majority_element = num
        #     count += (1 if majority_element == num else -1)
        
        # return majority_element

import unittest
class Test(unittest.TestCase):

    def test_example_1(self):
        solution = Solution()
        nums = [3,2,3]
        expected_output = 3
        actual_output = solution.majorityElement(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        expected_output = 2
        actual_output = solution.majorityElement(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2,3,3,3,3,3]
        expected_output = 3
        actual_output = solution.majorityElement(nums)
        self.assertEqual(actual_output, expected_output)

###################################
if __name__ == '__main__':
    unittest.main()
