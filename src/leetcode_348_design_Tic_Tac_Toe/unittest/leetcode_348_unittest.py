import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_348_helper import FunctionHelper
from solutions.leetcode_348_solution import TicTacToe


class Test(unittest.TestCase):
    def test_example_1(self):
        methods = [
            "TicTacToe",
            "move",
            "move",
            "move",
            "move",
            "move",
            "move",
            "move",
        ]
        args = [
            [3],
            [0, 0, 1],
            [0, 2, 2],
            [2, 2, 1],
            [1, 1, 2],
            [2, 0, 1],
            [1, 0, 2],
            [2, 1, 1],
        ]
        expected_output = [None, 0, 0, 0, 0, 0, 0, 1]

        actual_output = FunctionHelper(TicTacToe(args[0][0])).execute_methods(
            methods[1:], args[1:]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        methods = [
            "TicTacToe",
            "move",
            "move",
            "move",
            "move",
            "move",
            "move",
            "move",
            "move",
            "move",
        ]
        args = [
            [3],
            [0, 0, 1],
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 1, 1],
            [1, 2, 2],
            [2, 0, 1],
        ]
        expected_output = [None, 0, 0, 0, 0, 0, 0, 1]

        actual_output = FunctionHelper(TicTacToe(args[0][0])).execute_methods(
            methods[1:], args[1:]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        methods = ["TicTacToe", "move", "move", "move", "move", "move", "move"]
        args = [
            [3],
            [0, 0, 1],
            [0, 1, 2],
            [0, 2, 1],
            [1, 1, 2],
            [2, 0, 1],
            [2, 1, 2],
        ]
        expected_output = [None, 0, 0, 0, 0, 0, 2]

        actual_output = FunctionHelper(TicTacToe(args[0][0])).execute_methods(
            methods[1:], args[1:]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        methods = ["TicTacToe", "move", "move", "move", "move", "move", "move"]
        args = [[3], [0, 0, 1], [0, 1, 2], [0, 2, 1], [1, 1, 2], [2, 0, 1]]
        expected_output = [None, 0, 0, 0, 0, 0]

        actual_output = FunctionHelper(TicTacToe(args[0][0])).execute_methods(
            methods[1:], args[1:]
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
