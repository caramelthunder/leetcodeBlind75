import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_33_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        inputs = (
            [4,5,6,7,0,1,2],
            0
        )
        expected_output = 4
        actual_output = self.solution.search(*inputs)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        inputs = (
            [4,5,6,7,0,1,2],
            3
        )
        expected_output = -1
        actual_output = self.solution.search(*inputs)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        inputs = (
            [1],
            0
        )
        expected_output = -1
        actual_output = self.solution.search(*inputs)
        self.assertEqual(actual_output, expected_output)




######################################
if __name__ == '__main__':
    unittest.main()