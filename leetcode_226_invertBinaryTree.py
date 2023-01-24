'''
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

Output: [4,7,2,9,6,3,1]
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Helper:
    def numbers_to_tree(self, numbers: List[int]) -> TreeNode:
        if not numbers:
            return None
        nodes = iter(numbers)
        root = TreeNode(next(nodes))
        queue = [root]
        while queue:
            node = queue.pop(0)
            left_tree = next(nodes, None)
            if left_tree:
                node.left = TreeNode(left_tree)
                queue.append(node.left)

            right_tree = next(nodes, None)
            if right_tree:
                node.right = TreeNode(right_tree)
                queue.append(node.right)
        return root

    def tree_to_numbers(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        numbers = []
        while queue:
            node = queue.pop(0)
            numbers.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return numbers

class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)

        root.left = right_tree
        root.right = left_tree

        return root

from collections import deque
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            node.left, node.right = node.right , node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return root

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example1(self):
        params = [4,2,7,1,3,6,9]
        expected_output = [4,7,2,9,6,3,1]

        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.helper.tree_to_numbers(self.solution2.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output2, expected_output)

    def test_example2(self):
        params = [2,1,3]
        expected_output = [2,3,1]

        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.helper.tree_to_numbers(self.solution2.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output2, expected_output)

    def test_example3(self):
        params = []
        expected_output = []

        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.helper.tree_to_numbers(self.solution2.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output2, expected_output)

#################################
if __name__ == '__main__':
    unittest.main()
    
