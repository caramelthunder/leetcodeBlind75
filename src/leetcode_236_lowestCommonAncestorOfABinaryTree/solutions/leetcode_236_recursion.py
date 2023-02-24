from helpers.leetcode_236_helper import TreeNode

class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		if not root:
			return None
		
		if root in [p, q]:
			return root
		
		found_either_in_left = self.lowestCommonAncestor(root.left, p, q)
		found_either_in_right = self.lowestCommonAncestor(root.right, p, q)

		if found_either_in_left and found_either_in_right:
			return root
		
		return found_either_in_left or found_either_in_right
