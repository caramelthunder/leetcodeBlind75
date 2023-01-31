'''
https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        ans = ''

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            _sum = x + y + carry_over
            ans = str(_sum % 2) + ans
            carry_over = _sum // 2

            i -= 1
            j -= 1

        return '1' + ans if carry_over else ans
            

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        a, b = "11", "1"
        expected_output = "100"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        a, b = "1010", "1011"
        expected_output = "10101"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)
    
    def test_edge_case_1(self):
        a, b = "0", "0"
        expected_output = "0"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_2(self):
        a, b = "1", "1"
        expected_output = "10"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_3(self):
        a, b = "101", "11"
        expected_output = "1000"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)

#############################
if __name__ == '__main__':
    unittest.main()

