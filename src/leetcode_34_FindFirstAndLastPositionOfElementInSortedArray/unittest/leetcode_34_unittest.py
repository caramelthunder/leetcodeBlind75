import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_34_solution import Solution as Solution1


class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()

    def test_example_1(self):
        params = {"nums": [5, 7, 7, 8, 8, 10], "target": 8}
        expected_output = [3, 4]

        actual_output = self.solution1.searchRange(
            nums=params["nums"], target=params["target"]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {"nums": [5, 7, 7, 8, 8, 10], "target": 6}
        expected_output = [-1, -1]

        actual_output = self.solution1.searchRange(
            nums=params["nums"], target=params["target"]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = {"nums": [], "target": 0}
        expected_output = [-1, -1]

        actual_output = self.solution1.searchRange(
            nums=params["nums"], target=params["target"]
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        params = {"nums": [5, 7, 8, 8, 8, 10], "target": 8}
        expected_output = [2, 4]

        actual_output = self.solution1.searchRange(
            nums=params["nums"], target=params["target"]
        )
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
