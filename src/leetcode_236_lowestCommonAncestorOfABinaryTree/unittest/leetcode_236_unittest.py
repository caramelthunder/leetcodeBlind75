import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_236_helper import TreeHelper
from solutions.leetcode_236_recursion import Solution as Solution1
from solutions.leetcode_236_paths_intersection import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.treeHelper = TreeHelper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        arr, p_val, q_val, output_val = [3,5,1,6,2,0,8,None,None,7,4], 5, 1, 3
        root = self.treeHelper.arr_to_tree(arr)
        p, q = self.treeHelper.search(root, p_val), self.treeHelper.search(root, q_val)
        expected_output = self.treeHelper.search(root, output_val)

        actual_output = self.solution1.lowestCommonAncestor(root, p, q)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lowestCommonAncestor(root, p, q)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        arr, p_val, q_val, output_val = [3,5,1,6,2,0,8,None,None,7,4], 5, 4, 5
        root = self.treeHelper.arr_to_tree(arr)
        p, q = self.treeHelper.search(root, p_val), self.treeHelper.search(root, q_val)
        expected_output = self.treeHelper.search(root, output_val)

        actual_output = self.solution1.lowestCommonAncestor(root, p, q)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lowestCommonAncestor(root, p, q)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        arr, p_val, q_val, output_val = [1,2], 1, 2, 1
        root = self.treeHelper.arr_to_tree(arr)
        p, q = self.treeHelper.search(root, p_val), self.treeHelper.search(root, q_val)
        expected_output = self.treeHelper.search(root, output_val)

        actual_output = self.solution1.lowestCommonAncestor(root, p, q)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.lowestCommonAncestor(root, p, q)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()