import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_199_helper import TreeHelper
from solutions.leetcode_199_breadth_first import Solution as Solution1
from solutions.leetcode_199_depth_first import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.treeHelper = TreeHelper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        root = self.treeHelper.arr_to_tree([1,2,3,None,5,None,4])
        expected_output = [1,3,4]

        actual_output = self.solution1.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        root = self.treeHelper.arr_to_tree([1,None,3])
        expected_output = [1,3]

        actual_output = self.solution1.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        root = self.treeHelper.arr_to_tree([])
        expected_output = []

        actual_output = self.solution1.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

    def test_all_right_nodes(self):
        root = self.treeHelper.arr_to_tree([1,None,2,None,None,None,3,None,None,None,None,None,None,None,4])
        expected_output = [1,2,3,4]

        actual_output = self.solution1.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.rightSideView(root)
        self.assertEqual(actual_output, expected_output)
    
    def test_all_left_nodes(self):
        root = self.treeHelper.arr_to_tree([1,2,None,3,None,None,None,4])
        expected_output = [1,2,3,4]

        actual_output = self.solution1.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.rightSideView(root)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()