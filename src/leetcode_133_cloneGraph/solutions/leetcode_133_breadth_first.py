from helpers.leetcode_133_helper import GraphNode
from collections import deque

class Solution:
    def cloneGraph(self, node: GraphNode) -> GraphNode:
        if not node:
            return None
            
        first = node
        cloned_nodes = {}
        q = deque([first])

        while q:
            node = q.popleft()

            if node.val not in cloned_nodes:
                cloned_nodes[node.val] = GraphNode(node.val)

            for neighbor in node.neighbors:
                if neighbor.val not in cloned_nodes:
                    cloned_nodes[neighbor.val] = GraphNode(neighbor.val)
                    q.append(neighbor)
                cloned_nodes[node.val].neighbors.append(cloned_nodes[neighbor.val])

        return cloned_nodes[first.val]