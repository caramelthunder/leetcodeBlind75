from helpers.leetcode_98_helper import TreeNode

class Solution:
	def isValidBST(self, root: TreeNode):
		if not root:
			return True
		
		stack = [(root, float('-inf'), float('inf'))]

		while stack:
			node, left_bound, right_bound = stack.pop()

			if not (left_bound < node.val < right_bound):
				return False

			if node.right:
				stack.append((node.right, node.val, right_bound))
			if node.left:
				stack.append((node.left, left_bound, node.val))

		return True
