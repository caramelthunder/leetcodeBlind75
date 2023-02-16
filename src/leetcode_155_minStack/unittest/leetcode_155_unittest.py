import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_155_helper import Helper
from solutions.leetcode_155_two_stacks import MinStack as Solution1
from solutions.leetcode_155_one_stack_tuple import MinStack as Solution2
from solutions.leetcode_155_two_stacks_optimized import MinStack as Solution3

class Test(unittest.TestCase):

    def setUp(self):
        self.helper = Helper()
    
    def test_example_1(self):
        inputs = (
            ["MinStack","push","push","push","getMin","pop","top","getMin"],
            [[],[-2],[0],[-3],[],[],[],[]]
        )
        expected_output = [None,None,None,None,-3,None,0,-2]

        actual_output = self.helper.run_methods(Solution1(), *inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.helper.run_methods(Solution2(), *inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.helper.run_methods(Solution3(), *inputs)
        self.assertEqual(actual_output, expected_output)

    def test_push_pop(self):
        inputs = (
            ["MinStack", "push", "push", "pop", "push", "getMin", "pop", "top"],
            [[], [1], [2], None, [3], None, None, None]
        )
        expected_output = [None, None, None, None, None, 1, None, 1]

        actual_output = self.helper.run_methods(Solution1(), *inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.helper.run_methods(Solution2(), *inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.helper.run_methods(Solution3(), *inputs)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_minima(self):
        inputs = (
            ["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin", "pop", "getMin"],
            [[], [3], [1], [2], [1], None, None, None, None, None, None, None]
        )
        expected_output = [None, None, None, None, None, 1, None, 1, None, 1, None, 3]

        actual_output = self.helper.run_methods(Solution1(), *inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.helper.run_methods(Solution2(), *inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.helper.run_methods(Solution3(), *inputs)
        self.assertEqual(actual_output, expected_output)

###################################################
if __name__ == '__main__':
    unittest.main()
