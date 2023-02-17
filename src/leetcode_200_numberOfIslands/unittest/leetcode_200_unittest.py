import sys
import os
import unittest
import copy

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_200_depth_first import Solution as Solution1
from solutions.leetcode_200_breadth_first import Solution as Solution2
from solutions.leetcode_200_union_find import Solution as Solution3

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_example_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected_output = 1

        actual_output = self.solution1.numIslands(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numIslands(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numIslands(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        expected_output = 3

        actual_output = self.solution1.numIslands(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.numIslands(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.numIslands(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)


#######################################
if __name__ == '__main__':
    unittest.main()