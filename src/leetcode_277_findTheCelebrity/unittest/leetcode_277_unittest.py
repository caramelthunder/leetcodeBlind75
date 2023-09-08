import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_277_solution import Solution


class Test(unittest.TestCase):
    def test_example_1(self):
        graph = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
        expected_output = 1

        solution = Solution(graph)
        actual_output = solution.findCelebrity(len(graph))
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        graph = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
        expected_output = -1

        solution = Solution(graph)
        actual_output = solution.findCelebrity(len(graph))
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
