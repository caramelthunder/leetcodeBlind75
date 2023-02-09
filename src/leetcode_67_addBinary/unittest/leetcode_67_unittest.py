import unittest

import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_67_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        a, b = "11", "1"
        expected_output = "100"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        a, b = "1010", "1011"
        expected_output = "10101"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)
    
    def test_edge_case_1(self):
        a, b = "0", "0"
        expected_output = "0"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_2(self):
        a, b = "1", "1"
        expected_output = "10"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_3(self):
        a, b = "101", "11"
        expected_output = "1000"
        actual_output = self.solution.addBinary(a= a, b= b)
        self.assertEqual(actual_output, expected_output)

#############################
if __name__ == '__main__':
    unittest.main()
    

