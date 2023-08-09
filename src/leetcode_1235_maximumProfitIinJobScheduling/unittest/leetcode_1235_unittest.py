import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from solutions.leetcode_1235_dp_linear_search import Solution as LinearSolution
from solutions.leetcode_1235_dp_binary_search import (
    Solution as OptimalSolution,
)
from solutions.leetcode_1235_dp_binary_search_custom_object import (
    Solution as OptimalSolutionCustomObject,
)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.linear_solution = LinearSolution()
        self.optimal_solution = OptimalSolution()
        self.optimal_solution_custom_object = OptimalSolutionCustomObject()

    def test_example_1(self):
        input = {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 6],
            "profit": [50, 10, 40, 70],
        }
        expected_output = 120

        actual_output = self.linear_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution_custom_object.jobScheduling(
            **input
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        input = {
            "startTime": [1, 2, 3, 4, 6],
            "endTime": [3, 5, 10, 6, 9],
            "profit": [20, 20, 100, 70, 60],
        }
        expected_output = 150

        actual_output = self.linear_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution_custom_object.jobScheduling(
            **input
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        input = {
            "startTime": [1, 1, 1],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 4],
        }
        expected_output = 6

        actual_output = self.linear_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution_custom_object.jobScheduling(
            **input
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        input = {
            "startTime": [43, 13, 36, 31, 40, 5, 47, 13, 28, 16, 2, 11],
            "endTime": [44, 22, 41, 41, 47, 13, 48, 35, 48, 26, 21, 39],
            "profit": [8, 20, 3, 19, 16, 8, 11, 13, 2, 15, 1, 1],
        }
        expected_output = 66

        actual_output = self.linear_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution_custom_object.jobScheduling(
            **input
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_5(self):
        input = {
            "startTime": [1, 3, 3, 3, 5, 5, 13, 5],
            "endTime": [17, 14, 8, 11, 14, 7, 17, 9],
            "profit": [9, 3, 7, 18, 2, 17, 4, 6],
        }
        expected_output = 22

        actual_output = self.linear_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution_custom_object.jobScheduling(
            **input
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_6(self):
        input = {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 1000000000],
            "profit": [50, 10, 40, 70],
        }
        expected_output = 120

        actual_output = self.linear_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution.jobScheduling(**input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimal_solution_custom_object.jobScheduling(
            **input
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
