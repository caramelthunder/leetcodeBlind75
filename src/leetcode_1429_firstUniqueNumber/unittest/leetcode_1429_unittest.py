import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1429_double_linked_list import (
    FirstUnique as FirstUniqueDoubleLinkedList,
)
from solutions.leetcode_1429_using_deque import FirstUnique as FirstUniqueDeque
from helpers.leetcode_1429_helper import FunctionHelper


class Test(unittest.TestCase):
    def setUp(self):
        self.function_helper = FunctionHelper

    def test_example_1(self):
        input = {
            "method_names": [
                "FirstUnique",
                "showFirstUnique",
                "add",
                "showFirstUnique",
                "add",
                "showFirstUnique",
                "add",
                "showFirstUnique",
            ],
            "method_args": [[[2, 3, 5]], [], [5], [], [2], [], [3], []],
        }
        expected_output = [None, 2, None, 2, None, 3, None, -1]

        actual_output = FunctionHelper(
            FirstUniqueDoubleLinkedList, nums=input["method_args"][0][0]
        ).run(input["method_names"][1:], input["method_args"][1:])
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(
            FirstUniqueDeque, nums=input["method_args"][0][0]
        ).run(input["method_names"][1:], input["method_args"][1:])
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        input = {
            "method_names": [
                "FirstUnique",
                "showFirstUnique",
                "add",
                "add",
                "add",
                "add",
                "add",
                "showFirstUnique",
            ],
            "method_args": [
                [[7, 7, 7, 7, 7, 7]],
                [],
                [7],
                [3],
                [3],
                [7],
                [17],
                [],
            ],
        }
        expected_output = [None, -1, None, None, None, None, None, 17]

        actual_output = FunctionHelper(
            FirstUniqueDoubleLinkedList, nums=input["method_args"][0][0]
        ).run(input["method_names"][1:], input["method_args"][1:])
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(
            FirstUniqueDeque, nums=input["method_args"][0][0]
        ).run(input["method_names"][1:], input["method_args"][1:])
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        input = {
            "method_names": [
                "FirstUnique",
                "showFirstUnique",
                "add",
                "showFirstUnique",
            ],
            "method_args": [[[809]], [], [809], []],
        }
        expected_output = [None, 809, None, -1]

        actual_output = FunctionHelper(
            FirstUniqueDoubleLinkedList, nums=input["method_args"][0][0]
        ).run(input["method_names"][1:], input["method_args"][1:])
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(
            FirstUniqueDeque, nums=input["method_args"][0][0]
        ).run(input["method_names"][1:], input["method_args"][1:])
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
