import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1155_top_down_memoisation import Solution as Solution1
from solutions.leetcode_1155_bottom_up_tabulation import Solution as Solution2


class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        n, k, target = 1, 6, 3
        expected_output = 1

        actual_output = self.solution1.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        n, k, target = 2, 6, 7
        expected_output = 6

        actual_output = self.solution1.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        n, k, target = 30, 30, 500
        expected_output = 222616187

        actual_output = self.solution1.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        n, k, target = 3, 6, 7
        expected_output = 15

        actual_output = self.solution1.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numRollsToTarget(n, k, target)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()