import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_224_stack import Solution as SolutionStack
from solutions.leetcode_224_stack_str_reversed import (
    Solution as SolutionStackStrReversed,
)


class Test(unittest.TestCase):
    def setUp(self):
        self.sol_stack = SolutionStack()
        self.sol_stack_str_reversed = SolutionStackStrReversed()

    def test_example_1(self):
        s = "1 + 1"
        expected_ouptut = 2

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_example_2(self):
        s = " 2-1 + 2 "
        expected_ouptut = 3

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_example_3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected_ouptut = 23

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_example_4(self):
        s = "(1+(4+5+2)-3)-(6+8)"
        expected_ouptut = -5

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_example_5(self):
        s = "-(1+2)"
        expected_ouptut = -3

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_example_4(self):
        s = "-100"
        expected_ouptut = -100

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_example_5(self):
        s = "1--1"
        expected_ouptut = 2

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

    def test_large_number(self):
        s = "-1073741824 - 1073741824"
        expected_ouptut = -2147483648

        actual_output = self.sol_stack.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)

        actual_output = self.sol_stack_str_reversed.calculate(s)
        self.assertEqual(actual_output, expected_ouptut)


######################################
if __name__ == "__main__":
    unittest.main()
