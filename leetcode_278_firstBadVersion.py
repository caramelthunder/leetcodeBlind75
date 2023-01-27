'''
https://leetcode.com/problems/first-bad-version/
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 
Constraints:
1 <= bad <= n <= 231 - 1
'''

class Solution:
    def __init__(self, versions: list[bool]):
        self.versions = [False] + versions  # to add version 0.
    
    def isBadVersion(self, v: int) -> bool:
        return self.versions[v]

    def firstBadVersion(self, n: int):
        left, right = 1, n
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2

            if self.isBadVersion(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

import unittest
class Test(unittest.TestCase):
    def test_example_1(self):
        versions = [False, False, False, True, True]
        n = 5
        expected_output = 4
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        versions = [False, False, False, True, True, True, True, True, True, True, True]
        n = 11
        expected_output = 4
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_last_value(self):
        versions = [False, False, False, False, False, False, True]
        n = 7
        expected_output = 7
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_first_value(self):
        versions = [True, True, True]
        n = 3
        expected_output = 1
        solution = Solution(versions)
        actual_output = solution.firstBadVersion(n)
        self.assertEqual(actual_output, expected_output)

################################################
if __name__ == '__main__':
    unittest.main()
