import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_264_using_heap import Solution as Solution1
from solutions.leetcode_264_dynamic_programming import Solution as Solution2


class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        n = 10
        expected_output = 12

        actual_output = self.solution1.nthUglyNumber(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.nthUglyNumber(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        n = 1
        expected_output = 1

        actual_output = self.solution1.nthUglyNumber(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.nthUglyNumber(n)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()


'''
Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
'''