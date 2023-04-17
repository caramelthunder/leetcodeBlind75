class UnionFind:
    '''
    The time complexity of the find(), union(), and isConnected() methods of the UnionFind class is O(log n) on average, 
    where n is the number of nodes. This is due to path compression, which reduces the height of the tree. 
    The space complexity of the class is O(n), where n is the number of nodes, to store the parent dictionary.
    '''

    def __init__(self):
        # initialize the parent dictionary
        self.parents = {}
    
    def find(self, x):
        # find the parent of x using path compression
        x_parent = self.parents.get(x, x)

        if x_parent != x:
            x_parent = self.find(x_parent)
        
        # update the parent of x for future use
        self.parents[x] = x_parent
        return x_parent
    
    def union(self, x, y):
        # union the sets containing x and y by setting their parents to the same value
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent != y_parent:
            self.parents[y_parent] = x_parent
    
    def isConnected(self, x, y):
        # check if x and y are in the same set by comparing their parents
        x_parent = self.find(x)
        y_parent = self.find(y)

        return x_parent == y_parent

class Solution:
    '''
    This code implements the Kruskal's algorithm to find the minimum spanning tree of a graph. 
    The Union-Find data structure is used to keep track of the connected components of the graph.

    The time complexity:    O(m log m)  , where m is the number of edges in the graph.
    The space complexity:   O(n)        , where n is the number of nodes in the graph.
    '''

    def minimumCost(self, n: int, connections: list[int]) -> int:
        # sort the connections by cost in ascending order
        connections.sort(key= lambda x: x[2])
        
        checked_connections = 0
        total_cost = 0
        UF = UnionFind()

        # iterate over the connections in ascending order of cost
        for src, dst, cost in connections:

            # if the source and destination are not already connected, 
            # connect them and add the cost
            if not UF.isConnected(src, dst):
                UF.union(src, dst)
                total_cost += cost
                checked_connections += 1

        # When all citites are connected by unique conections, a "Minimum-Spanning-Tree" is formed.
        # a MST always have n - 1 edges, when n is number of nodes.
        # if all nodes are connected, return the total cost; otherwise, return -1
        return total_cost if checked_connections == n - 1 else -1
