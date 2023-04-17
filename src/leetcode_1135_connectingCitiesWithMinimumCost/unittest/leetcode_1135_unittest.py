import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1135_union_find_sorting import Solution as Solution1
from solutions.leetcode_1135_union_find_minheap import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "n":3,
            "connections": [[1,2,5],[1,3,6],[2,3,1]]
        }
        expected_output = 6

        actual_output = self.sol1.minimumCost(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol1.minimumCost(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            "n":4,
            "connections": [[1,2,3],[3,4,4]]
        }
        expected_output = -1

        actual_output = self.sol1.minimumCost(**params)
        self.assertEqual(actual_output, expected_output)
        
        actual_output = self.sol1.minimumCost(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = {
            "n":4,
            "connections": [[1,2,1],[1,3,2],[3,4,4],[1,4,3]]
        }
        expected_output = 6

        actual_output = self.sol1.minimumCost(**params)
        self.assertEqual(actual_output, expected_output)
        
        actual_output = self.sol1.minimumCost(**params)
        self.assertEqual(actual_output, expected_output)



######################################
if __name__ == '__main__':
    unittest.main()