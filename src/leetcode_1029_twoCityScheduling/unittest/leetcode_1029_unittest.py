import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1029_solution import Solution

class Test(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        expected_output = 110

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        expected_output = 1859

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
        expected_output = 3086

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)

    def test_min_max_cost(self):
        costs = [[1, 1000], [1000, 1]]
        expected_output = 2

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)

    def test_equal_cost(self):
        costs = [[10, 10], [10, 10]]
        expected_output = 20

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)

    def test_sorted_by_difference(self):
        costs = [[10, 20], [20, 30]]
        expected_output = 40

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)

    def test_sorted_reverse_by_difference(self):
        costs = [[30, 20], [20, 10]]
        expected_output = 40

        actual_output = self.solution.twoCitySchedCost(costs)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()