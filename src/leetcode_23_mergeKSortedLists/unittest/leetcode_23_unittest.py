import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_23_in_place_heap import Solution as Solution1
from solutions.leetcode_23_divide_and_conquer import Solution as Solution2
from helpers.leetcode_23_helper import ListNodeHelper


class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.arr_to_linked_list = ListNodeHelper().arr_to_linked_list
        self.linked_list_to_arr = ListNodeHelper().linked_list_to_arr

    def test_example_1(self):
        input = [[1, 4, 5], [1, 3, 4], [2, 6]]
        expected_output = [1, 1, 2, 3, 4, 4, 5, 6]

        actual_output = self.linked_list_to_arr(
            self.solution1.mergeKLists(
                [self.arr_to_linked_list(arr) for arr in input]
            )
        )
        self.assertEqual(actual_output, expected_output)

        actual_output = self.linked_list_to_arr(
            self.solution2.mergeKLists(
                [self.arr_to_linked_list(arr) for arr in input]
            )
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        input = []
        expected_output = []

        actual_output = self.linked_list_to_arr(
            self.solution1.mergeKLists(
                [self.arr_to_linked_list(arr) for arr in input]
            )
        )
        self.assertEqual(actual_output, expected_output)

        actual_output = self.linked_list_to_arr(
            self.solution2.mergeKLists(
                [self.arr_to_linked_list(arr) for arr in input]
            )
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        input = [[]]
        expected_output = []

        actual_output = self.linked_list_to_arr(
            self.solution1.mergeKLists(
                [self.arr_to_linked_list(arr) for arr in input]
            )
        )
        self.assertEqual(actual_output, expected_output)

        actual_output = self.linked_list_to_arr(
            self.solution2.mergeKLists(
                [self.arr_to_linked_list(arr) for arr in input]
            )
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
