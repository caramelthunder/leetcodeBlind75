import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_70_topdown_memoisation import Solution as Solution1
from solutions.leetcode_70_bottomup_tabulation import Solution as Solution2
from solutions.leetcode_70_bottomup_space_optimized import Solution as Solution3

class Test(unittest.TestCase):
    def setUp(self):
        self.solution_top_down = Solution1()
        self.solution_bottom_up = Solution2()
        self.solution_bottom_up_constant_space = Solution3()
    
    def test_example_1(self):
        n = 2
        expected_output = 2

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

    def test_example_2(self):
        n = 3
        expected_output = 3

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

    def test_example_3(self):
        n = 5
        expected_output = 8

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

    def test_example_4(self):
        n = 6
        expected_output = 13

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

#########################
if __name__ == '__main__':
    unittest.main()
