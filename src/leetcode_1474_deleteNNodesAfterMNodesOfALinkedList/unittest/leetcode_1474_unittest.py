import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1474_solution import Solution
from helpers.leetcode_1474_helper import LinkedListHelper


class Test(unittest.TestCase):
    def setUp(self):
        self.linked_list_helper = LinkedListHelper()
        self.solution = Solution()

    def test_example_1(self):
        head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        m = 2
        n = 3

        expected_output = [1, 2, 6, 7, 11, 12]

        actual_output = self.linked_list_helper.list_to_arr(
            self.solution.deleteNodes(
                self.linked_list_helper.arr_to_list(head), m, n
            )
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        m = 1
        n = 3

        expected_output = [1, 5, 9]

        actual_output = self.linked_list_helper.list_to_arr(
            self.solution.deleteNodes(
                self.linked_list_helper.arr_to_list(head), m, n
            )
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        head = [1, 2, 3, 4, 5, 6]
        m = 2
        n = 2

        expected_output = [1, 2, 5, 6]

        actual_output = self.linked_list_helper.list_to_arr(
            self.solution.deleteNodes(
                self.linked_list_helper.arr_to_list(head), m, n
            )
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
