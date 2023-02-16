import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_98_helper import TreeHelper
from solutions.leetcode_98_recursive import Solution as Solution1
from solutions.leetcode_98_iterative import Solution as Solution2
from solutions.leetcode_98_inorder import Solution as Solution3

class Test(unittest.TestCase):

	def setUp(self):
		self.treeHelper = TreeHelper()
		self.solution1 = Solution1()
		self.solution2 = Solution2()
		self.solution3 = Solution3()

	def test_example_1(self):
		arr = [2,1,3,None,None,None,None]
		expected_output = True

		actual_output = self.solution1.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution2.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution3.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

	def test_example_2(self):
		arr = [5,1,4,None,None,3,6,None,None,None,None,None,None,None,None]
		expected_output = False

		actual_output = self.solution1.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution2.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution3.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)
	
	def test_single_node_tree(self):
		arr = [5, None, None]
		expected_output = True

		actual_output = self.solution1.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution2.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution3.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)
	
	def test_complete_binary_tree(self):
		arr = [4, 2, 6, 1, 3, 5, 7]
		expected_output = True

		actual_output = self.solution1.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution2.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution3.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

	def test_unbalanced_binary_tree(self):
		arr = [4, 2, 5, 1, None, None, 6]
		expected_output = True

		actual_output = self.solution1.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution2.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

		actual_output = self.solution3.isValidBST(self.treeHelper.arr_to_tree(arr))
		self.assertEqual(actual_output, expected_output)

################################
if __name__ == '__main__':
	unittest.main()