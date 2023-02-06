import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_102_helper import TreeHelper
from solutions.leetcode_102_depth_first import Solution as DFS
from solutions.leetcode_102_breadth_first import Solution as BFS

class Test(unittest.TestCase):
    def setUp(self):
        self.treeHelper = TreeHelper()
        self.dfs = DFS()
        self.bfs = BFS()

    def test_example_1(self):
        arr = [3,9,20,None,None,15,7]
        expected_output = [[3],[9,20],[15,7]]

        actual_output = self.bfs.levelOrder(self.treeHelper.arr_to_tree(arr, 0))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.dfs.levelOrder(self.treeHelper.arr_to_tree(arr, 0))
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        arr = [1]
        expected_output = [[1]]

        actual_output = self.bfs.levelOrder(self.treeHelper.arr_to_tree(arr, 0))
        self.assertEqual(actual_output, expected_output)
        
        actual_output = self.dfs.levelOrder(self.treeHelper.arr_to_tree(arr, 0))
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        arr = []
        expected_output = []

        actual_output = self.bfs.levelOrder(self.treeHelper.arr_to_tree(arr, 0))
        self.assertEqual(actual_output, expected_output)
        
        actual_output = self.dfs.levelOrder(self.treeHelper.arr_to_tree(arr, 0))
        self.assertEqual(actual_output, expected_output)
        

######################################
if __name__ == '__main__':
    unittest.main()

