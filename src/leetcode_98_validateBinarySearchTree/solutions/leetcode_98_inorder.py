from helpers.leetcode_98_helper import TreeNode

class Solution:
	def isValidBST(self, root: TreeNode):
		if not root:
			return True
		
		def dfs(node, inorder):
			if not node:
				return 

			dfs(node.left, inorder)
			inorder.append(node.val)
			dfs(node.right, inorder)
		
		inorder = []
		dfs(root, inorder)

		for i in range(len(inorder) - 1):
			if inorder[i] >= inorder[i + 1]:
				return False
		return True
