import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_279_top_down_memoisation import Solution as Solution1
from solutions.leetcode_279_bottom_up_tabulation import Solution as Solution2
from solutions.leetcode_279_breadth_first import Solution as Solution3


class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
    
    def test_example_1(self):
        n = 12
        expected_output = 3

        actual_output = self.solution1.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numSquares(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        n = 13
        expected_output = 2

        actual_output = self.solution1.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numSquares(n)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        n = 10000
        expected_output = 1

        actual_output = self.solution1.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numSquares(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        n = 5360
        expected_output = 4

        actual_output = self.solution1.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numSquares(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_5(self):
        n = 2167
        expected_output = 4

        actual_output = self.solution1.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numSquares(n)
        self.assertEqual(actual_output, expected_output)

    def test_example_6(self):
        n = 9997
        expected_output = 2

        actual_output = self.solution1.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numSquares(n)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numSquares(n)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()