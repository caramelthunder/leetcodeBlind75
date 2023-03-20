class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return [node for node in range(n)]

        degrees = [0 for _ in range(n)]
        graph = {node: [] for node in range(n)}
        self.build_graph( edges, graph, degrees)

        node_cnt = n
        leaves = [node for node in range(n) if degrees[node] == 1]

        while node_cnt > 2:
            new_leaves = []

            while leaves:
                node = leaves.pop()
                node_cnt -= 1

                for parent in graph[node]:
                    degrees[parent] -= 1
                    if degrees[parent] == 1:
                        new_leaves.append(parent)
            
            leaves = new_leaves
 
        return leaves

    def build_graph(self, edges, graph, degrees):
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            degrees[a] += 1
            degrees[b] += 1