from collections import deque

class Solution:
    '''
    Define a function called minReorder that takes an integer n and a list of lists of integers 
    called connections as arguments, and returns an integer.

    Time complexity analysis: O(V+E)
    minReorder calls the build_graph function, which iterates over all edges in the connections list. 
    Therefore, the time complexity of build_graph is O(E), where E is the number of edges in connections.
    minReorder uses a breadth-first search (BFS) algorithm to traverse the graph, 
    which takes O(V+E) time, where V is the number of nodes in the graph. 
    Therefore, the time complexity of minReorder is also O(V+E).
    
    Space complexity analysis: O(V+E)
    The build_graph function creates two dictionaries: `adj_list` and `out_degree_map`

    '''
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Call the build_graph function and store the returned adjacency list and out-degree map in variables
        adj_list, out_degree_map = self.build_graph(n, connections)

        # Initialize a count variable called cnt to 0
        cnt = 0
        # Initialize a set called visited and add the first node (0) to it
        visited = set([0])
        # Initialize a deque called q and add the first node (0) and a False value to it
        q = deque([(0, False)])

        # While there are still nodes in the queue
        while q:
            # Pop the leftmost node and its corresponding redirect value from the queue
            curr, redirect = q.popleft()
            # Increment cnt by the redirect value
            cnt += int(redirect)

            # For each neighbor of the current node
            for neighbor in adj_list[curr]:
                # If the neighbor hasn't been visited before
                if neighbor not in visited:
                    # Add the neighbor to the visited set
                    visited.add(neighbor)

                    # If the current node is an out-degree node of the neighbor
                    if neighbor in out_degree_map[curr]:
                        # Append the neighbor to the queue with a True redirect value
                        q.append((neighbor, True))
                    else:
                        # Append the neighbor to the queue with a False redirect value
                        q.append((neighbor, False))
            
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
