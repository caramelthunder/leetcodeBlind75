import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_146_solution import LRUCache
from helpers.leetcode_146_helper import Helper

class Test(unittest.TestCase):

    def setUp(self):
        self.helper = Helper()

    def test_example_1(self):
        params = (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        )
        expected_output = [None, None, None, 1, None, -1, None, -1, 3, 4]
        
        solution = LRUCache(*params[1][0])
        actual_output = self.helper.run_methods(solution, *params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = (
            ["LRUCache","put","put","get","put","put","get"],
            [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
        )
        expected_output = [None, None, None, 2, None, None, -1]
        
        solution = LRUCache(*params[1][0])
        actual_output = self.helper.run_methods(solution, *params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = (
            ["LRUCache","get","put","get","put","put","get","get"],
            [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
        )
        expected_output = [None, -1, None, -1, None, None, 2, 6]
        
        solution = LRUCache(*params[1][0])
        actual_output = self.helper.run_methods(solution, *params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_4(self):
        params = (
            ["LRUCache","put","put","put","put","get","get"], 
            [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
        )
        expected_output = [None, None, None, None, None, -1, 3]
        
        solution = LRUCache(*params[1][0])
        actual_output = self.helper.run_methods(solution, *params)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()