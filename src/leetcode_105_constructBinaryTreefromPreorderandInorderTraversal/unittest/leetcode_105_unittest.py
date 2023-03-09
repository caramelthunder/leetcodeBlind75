import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_105_helper import TreeHelper
from solutions.leetcode_105_reference_passing import Solution as Solution1
from solutions.leetcode_105_divide_conquer import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.treeHelper = TreeHelper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        expected_output = [3,9,20,None,None,15,7]

        tree = self.solution1.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)

        tree = self.solution2.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        preorder = [-1]
        inorder = [-1]
        expected_output = [-1]

        tree = self.solution1.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)

        tree = self.solution2.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        preorder = [2,1]
        inorder = [1,2]
        expected_output = [2,1]

        tree = self.solution1.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)

        tree = self.solution2.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        preorder = [1,2]
        inorder = [1,2]
        expected_output = [1]

        tree = self.solution1.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)
        self.assertEqual(actual_output, expected_output)

        tree = self.solution2.buildTree(preorder, inorder)
        actual_output = self.treeHelper.tree_to_arr(tree)

######################################
if __name__ == '__main__':
    unittest.main()