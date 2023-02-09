from helpers.leetcode_133_helper import GraphNode

class Solution:
    def cloneGraph(self, node: GraphNode) -> GraphNode:
        return self._cloneGraph(node, {})
    
    def _cloneGraph(self, node: GraphNode, cloned_nodes: dict[int, GraphNode]) -> GraphNode:
        if not node:
            return None

        if node.val in cloned_nodes:
            return  cloned_nodes[node.val]
        
        cloned_node = GraphNode(node.val)
        cloned_nodes[node.val] = cloned_node

        for neighbor in node.neighbors:
            cloned_neighbor = self._cloneGraph(neighbor, cloned_nodes)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node