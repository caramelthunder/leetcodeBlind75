import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1466_bfs import Solution as Solution1
from solutions.leetcode_1466_dfs import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "n": 6,
            "connections": [[0,1],[1,3],[2,3],[4,0],[4,5]]
        }
        expected_output = 3

        actual_output = self.sol1.minReorder(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minReorder(**params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        params = {
            "n": 5,
            "connections": [[1,0],[1,2],[3,2],[3,4]]
        }
        expected_output = 2

        actual_output = self.sol1.minReorder(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minReorder(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = {
            "n": 3,
            "connections": [[1,0],[2,0]]
        }
        expected_output = 0

        actual_output = self.sol1.minReorder(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minReorder(**params)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()
