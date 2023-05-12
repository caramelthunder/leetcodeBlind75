import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_29_pow_of_two_DP import Solution as Solution1
from solutions.leetcode_29_pow_of_two_bit_shifting import Solution as Solution2


class Test(unittest.TestCase):
    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        dividend, divisor = 10, 3
        expected_output = 3

        actual_output = self.sol1.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        dividend, divisor = 7, -3
        expected_output = -2

        actual_output = self.sol1.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        dividend, divisor = 2**31 - 1, 2
        expected_output = (2**31 - 1) // 2

        actual_output = self.sol1.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        dividend, divisor = -(2**31), 4
        expected_output = -(2**31) // 4

        actual_output = self.sol1.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

    def test_example_6(self):
        dividend, divisor = -(2**31), -1
        expected_output = 2**31 - 1

        actual_output = self.sol1.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.divide(dividend=dividend, divisor=divisor)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
