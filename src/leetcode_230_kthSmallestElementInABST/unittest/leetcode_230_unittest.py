import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_230_helper import TreeHelper
from solutions.leetcode_230_inorder_traversal import Solution as Solution1
from solutions.leetcode_230_iterative import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.treeHelper = TreeHelper()
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "root": self.treeHelper.arr_to_tree([3,1,4,None,2]),
            "k": 1
        }
        expected_output = 1

        actual_output = self.sol1.kthSmallest(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.kthSmallest(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            "root": self.treeHelper.arr_to_tree([5,3,6,2,4,None,None,1]),
            "k": 3
        }
        expected_output = 3

        actual_output = self.sol1.kthSmallest(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.kthSmallest(**params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        params = {
            "root": self.treeHelper.arr_to_tree([1,None,3,None,None,2,5,None,None,None,None,None,None,4,8]),
            "k": 4
        }
        expected_output = 4

        actual_output = self.sol1.kthSmallest(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.kthSmallest(**params)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()
