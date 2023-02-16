from helpers.leetcode_98_helper import TreeNode

class Solution:
	def isValidBST(self, root: TreeNode):
		return self._isValidBST(root)
	
	def _isValidBST(self, node, left_bound= float('-inf'), right_bound= float('inf')):
		if not node:
			return True
		
		left_isBST = self._isValidBST(node.left, left_bound, node.val)
		right_isBST = self._isValidBST(node.right, node.val, right_bound)
		node_isBST = left_isBST and right_isBST and (left_bound < node.val < right_bound)

		return node_isBST