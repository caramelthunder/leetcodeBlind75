class GraphNode:
    def __init__(self, val= 0, neighbors= None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

from collections import deque
class GraphHelper:
    def adjLst_to_graph(self, adjLst: list[list[int]]) -> GraphNode:
        if not adjLst:
            return None
            
        first = GraphNode(1)
        created_nodes = {1: first}
        q = deque([first])

        while q:
            node = q.popleft()
            for val in adjLst[node.val - 1]:
                if val not in created_nodes:
                    created_nodes[val] = GraphNode(val)
                    q.append(created_nodes[val])
                node.neighbors.append(created_nodes[val])
        
        return first
                
    def graph_to_adjLst(self, graph: GraphNode ) -> list[list[int]]:
        if not graph:
            return []

        adjLst = []
        q = deque([graph])

        while q:
            node = q.popleft()
            for _ in range(node.val - len(adjLst)):
                adjLst.append([])
            
            for neihgbor in node.neighbors:
                adjLst[node.val - 1].append(neihgbor.val)
                if neihgbor.val > len(adjLst):
                    q.append(neihgbor)
            
        return adjLst