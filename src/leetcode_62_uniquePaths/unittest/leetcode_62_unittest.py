import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_62_top_down_memoisation import Solution as Solution1
from solutions.leetcode_62_bottom_up_tabulation import Solution as Solution2


class Test(unittest.TestCase):
    
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        m, n = 3, 7
        expected_output = 28

        actual_output = self.solution1.uniquePaths(m, n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.uniquePaths(m, n)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        m, n = 3, 2
        expected_output = 3

        actual_output = self.solution1.uniquePaths(m, n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.uniquePaths(m, n)
        self.assertEqual(actual_output, expected_output)



######################################
if __name__ == '__main__':
    unittest.main()