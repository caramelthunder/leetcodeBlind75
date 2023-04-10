import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_456_brute_force import Solution as Solution1
from solutions.leetcode_456_monotonic_stack import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_0(self):
        nums = [1,3,2,4,5,6,7,8,9,10]
        expected_output = True

        actual_output = self.solution1.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_1(self):
        nums = [1,2,3,4]
        expected_output = False

        actual_output = self.solution1.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [3,1,4,2]
        expected_output = True

        actual_output = self.solution1.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = [-1,3,2,0]
        expected_output = True

        actual_output = self.solution1.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.find132pattern(nums= nums)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()