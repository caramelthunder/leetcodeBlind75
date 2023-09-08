import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_1396_helper import FunctionHelper
from solutions.leetcode_1396_custom_object import (
    UndergroundSystem as CustomObjectSolution,
)
from solutions.leetcode_1396_hash_table import (
    UndergroundSystem as HashTableSolution,
)


class Test(unittest.TestCase):
    def test_example_1(self):
        method_names = [
            "UndergroundSystem",
            "checkIn",
            "checkIn",
            "checkIn",
            "checkOut",
            "checkOut",
            "checkOut",
            "getAverageTime",
            "getAverageTime",
            "checkIn",
            "getAverageTime",
            "checkOut",
            "getAverageTime",
        ]
        method_args = [
            [],
            [45, "Leyton", 3],
            [32, "Paradise", 8],
            [27, "Leyton", 10],
            [45, "Waterloo", 15],
            [27, "Waterloo", 20],
            [32, "Cambridge", 22],
            ["Paradise", "Cambridge"],
            ["Leyton", "Waterloo"],
            [10, "Leyton", 24],
            ["Leyton", "Waterloo"],
            [10, "Waterloo", 38],
            ["Leyton", "Waterloo"],
        ]
        expected_output = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            14.00000,
            11.00000,
            None,
            11.00000,
            None,
            12.00000,
        ]

        actual_output = FunctionHelper(CustomObjectSolution()).invoke_methods(
            method_names[1:], method_args[1:]
        )
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(HashTableSolution()).invoke_methods(
            method_names[1:], method_args[1:]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        method_names = [
            "UndergroundSystem",
            "checkIn",
            "checkOut",
            "getAverageTime",
            "checkIn",
            "checkOut",
            "getAverageTime",
            "checkIn",
            "checkOut",
            "getAverageTime",
        ]
        method_args = [
            [],
            [10, "Leyton", 3],
            [10, "Paradise", 8],
            ["Leyton", "Paradise"],
            [5, "Leyton", 10],
            [5, "Paradise", 16],
            ["Leyton", "Paradise"],
            [2, "Leyton", 21],
            [2, "Paradise", 30],
            ["Leyton", "Paradise"],
        ]
        expected_output = [
            None,
            None,
            None,
            5.00000,
            None,
            None,
            5.50000,
            None,
            None,
            6.666666666666667,
        ]

        actual_output = FunctionHelper(CustomObjectSolution()).invoke_methods(
            method_names[1:], method_args[1:]
        )
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(HashTableSolution()).invoke_methods(
            method_names[1:], method_args[1:]
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
