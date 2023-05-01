import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_297_solution import Codec
from helpers.leetcode_297_helper import TreeHelper

class Test(unittest.TestCase):
    def setUp(self):
        self.ser = Codec()
        self.deser = Codec()
        self.treeHeler = TreeHelper()
    
    def test_example_1(self):
        expected_output = [1,2,3,'null','null',4,5]
        root = self.treeHeler.arr_to_tree(expected_output)

        actual_output = self.treeHeler.tree_to_arr(self.deser.deserialize(self.ser.serialize(root)))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        expected_output = []
        root = self.treeHeler.arr_to_tree(expected_output)

        actual_output = self.treeHeler.tree_to_arr(self.deser.deserialize(self.ser.serialize(root)))
        self.assertEqual(actual_output, expected_output)

    



######################################
if __name__ == '__main__':
    unittest.main()

'''
Example 1:

            1
           / \
          2   3
             / \
            4   5

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
'''