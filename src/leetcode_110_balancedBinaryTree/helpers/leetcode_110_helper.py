from collections import deque

class TreeNode:
   def __init__(self, val, left= None, right= None):
      self.val = val
      self.left = left
      self.right = right

class Helper:
   def nums_to_tree(self, nums: list[int]) -> TreeNode:
      if not nums:
         return None

      def dfs(nums, i):
         if not nums or i >= len(nums) or nums[i] == 'null':
            return None
         
         node = TreeNode(nums[i])
         node.left = dfs(nums, i * 2 + 1)
         node.right = dfs(nums, i * 2 + 2)

         return node

      root = dfs(nums, 0)
      return root

   def tree_to_nums(self, root: TreeNode) -> list[int]:
      if not root:
         return []
      
      nums = []
      q = deque([root])
      while q:
         level_len = len(q)
         level = []
         for _ in range(level_len):
            node = q.popleft()
            if node != 'null':
               level.append(node.val)
               for child in [node.left, node.right]:
                  if child:
                     q.append(child)
                  else:
                     q.append('null')
            else:
               level.append(node)
         nums.append(level)
      return nums