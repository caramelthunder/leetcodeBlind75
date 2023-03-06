import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_416_memoisation import Solution as Solution1
from solutions.leetcode_416_tabulation import Solution as Solution2
from solutions.leetcode_416_tabulation_space_optimized import Solution as Solution3


class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_example_1(self):
        nums = [1,5,11,5]
        expected_output = True

        actual_output = self.solution1.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.canPartition(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        nums = [1,2,3,5]
        expected_output = False

        actual_output = self.solution1.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = [2, 7, 11, 17, 23, 31, 35, 47, 59]
        expected_output = True

        actual_output = self.solution1.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.canPartition(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_4(self):
        nums = [3, 7, 9, 13, 21, 25, 29, 33]
        expected_output = True

        actual_output = self.solution1.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.canPartition(nums)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()