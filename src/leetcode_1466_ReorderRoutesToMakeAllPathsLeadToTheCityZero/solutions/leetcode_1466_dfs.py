class Solution:
    '''
    Define a function called minReorder that takes an integer n and a list of lists of integers 
    called connections as arguments, and returns an integer

    Time complexity analysis: O(V+E)
    
    Space complexity analysis: O(V+E)
    The build_graph function creates two dictionaries: `adj_list` and `out_degree_map`
    '''
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Call the build_graph function and store the returned adjacency list and out-degree map in variables
        adj_list, out_degree_map = self.build_graph(n, connections)
        # Initialize an empty set called visited
        visited = set()

        # Define a recursive function called dfs that takes a node called curr as an argument, 
        # and returns the number of edges that need to be redirected to reach all nodes in the graph
        def dfs(curr):
            # Add the current node to the visited set
            visited.add(curr)
            # Initialize a count variable called cnt to 0
            cnt = 0

            # For each neighbor of the current node
            for neighbor in adj_list[curr]:
                # If the neighbor hasn't been visited before
                if neighbor not in visited:
                    # If the current node is an out-degree node of the neighbor, increment cnt by 1
                    if neighbor in out_degree_map[curr]:
                        cnt += 1
                    # Recursively call dfs on the neighbor and add the returned value to cnt
                    cnt += dfs(neighbor)

            # Return cnt
            return cnt

        # Call dfs on the first node (0) and store the returned value in cnt
        cnt = dfs(0)
        # If all nodes have been visited, return cnt. Otherwise, return -1.
        return cnt if len(visited) == n else -1

    # Define a function called build_graph that takes an integer n and a list of lists of integers 
    # called edges as arguments, and returns a tuple of an adjacency list and an out-degree map
    def build_graph(self, n, edges):
        # Initialize an empty dictionary called adj_list
        adj_list = {node: [] for node in range(n)}
        # Initialize an empty dictionary called out_degree_map
        out_degree_map = {node: set() for node in range(n)}

        # For each edge in the edges list
        for a, b in edges:
            # Add node b to the adjacency list of node a, and add node a to the adjacency list of node b
            adj_list[a].append(b)
            adj_list[b].append(a)

            # Add node b to the out-degree set of node a
            out_degree_map[a].add(b)

        # Return the adjacency list and out-degree map as a tuple
        return (adj_list, out_degree_map)
