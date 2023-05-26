import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_295_solution import MedianFinder
from helpers.leetcode_295_helper import Helper


class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()

    def test_example_1(self):
        operation_queue = {
            "method_names": [
                "MedianFinder",
                "addNum",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            "method_args": [[], [1], [2], [], [3], []],
        }
        expected_output = [None, None, None, 1.5, None, 2.0]

        actual_output = self.helper.function_helper(
            MedianFinder(), **operation_queue
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        operation_queue = {
            "method_names": [
                "MedianFinder",
                "addNum",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            "method_args": [[], [1], [2], [], [3], [], [2], []],
        }
        expected_output = [None, None, None, 1.5, None, 2.0, None, 2.0]

        actual_output = self.helper.function_helper(
            MedianFinder(), **operation_queue
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        operation_queue = {
            "method_names": [
                "MedianFinder",
                "addNum",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            "method_args": [[], [1], [2], [], [3], [], [1], []],
        }
        expected_output = [None, None, None, 1.5, None, 2.0, None, 1.5]

        actual_output = self.helper.function_helper(
            MedianFinder(), **operation_queue
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        operation_queue = {
            "method_names": [
                "MedianFinder",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            "method_args": [
                [],
                [6],
                [],
                [10],
                [],
                [2],
                [],
                [6],
                [],
                [5],
                [],
                [0],
                [],
                [6],
                [],
                [3],
                [],
                [1],
                [],
                [0],
                [],
                [0],
                [],
            ],
        }
        expected_output = [
            None,
            None,
            6.00000,
            None,
            8.00000,
            None,
            6.00000,
            None,
            6.00000,
            None,
            6.00000,
            None,
            5.50000,
            None,
            6.00000,
            None,
            5.50000,
            None,
            5.00000,
            None,
            4.00000,
            None,
            3.00000,
        ]

        actual_output = self.helper.function_helper(
            MedianFinder(), **operation_queue
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
