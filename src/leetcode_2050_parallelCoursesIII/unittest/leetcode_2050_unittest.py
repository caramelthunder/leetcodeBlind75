import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_2050_breadth_first import Solution as Solution1
from solutions.leetcode_2050_depth_first import Solution as Solution2


class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        params = (
            3,
            [[1,3],[2,3]],
            [3,2,5]
        )
        expected_output = 8

        actual_output = self.solution1.minimumTime(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.minimumTime(*params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        params = (
            5,
            [[1,5],[2,5],[3,5],[3,4],[4,5]],
            [1,2,3,4,5]
        )
        expected_output = 12

        actual_output = self.solution1.minimumTime(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.minimumTime(*params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = (
            9,
            [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]],
            [9,5,9,5,8,7,7,8,4]
        )
        expected_output = 32

        actual_output = self.solution1.minimumTime(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.minimumTime(*params)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()