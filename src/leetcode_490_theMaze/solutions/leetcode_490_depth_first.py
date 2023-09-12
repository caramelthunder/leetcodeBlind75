from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        """
        Determines if there is a valid path in the maze from the start point to the destination point using Depth-First Search (DFS).

        Parameters:
        maze (List[List[int]]): A 2D grid representing the maze where 0 indicates an open path and 1 indicates a wall.
        start (List[int]): The starting point represented as [row, col].
        destination (List[int]): The destination point represented as [row, col].

        Returns:
        bool: True if there is a path from start to destination, False otherwise.

        Time Complexity:
        The time complexity is O(m⋅n⋅(m+n)) where m is the number of rows and n is the number of columns in the maze.

        Space Complexity:
        The space complexity is O(m*n) due to the additional space required to store the visited nodes and the recursion stack.
        """

        def rolling(
            curr: tuple[int, int], direction: tuple[int, int]
        ) -> tuple[int, int]:
            """Computes the next position by "rolling" in the given direction until hitting a wall or boundary."""
            curr_row, curr_col = curr
            _r, _c = direction
            while (
                0 <= curr_row + _r < rows
                and 0 <= curr_col + _c < cols
                and maze[curr_row + _r][curr_col + _c] == 0
            ):
                curr_row += _r
                curr_col += _c
            return curr_row, curr_col

        def dfs(curr: tuple[int, int]) -> bool:
            """Performs a depth-first search from the current position to find a path to the destination."""
            if curr == destination:
                return True
            if curr in visited or curr in visiting:
                return False

            visiting.add(curr)
            for _r, _c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_pos = rolling(curr, (_r, _c))
                if dfs(next_pos):
                    return True
            visiting.remove(curr)
            visited.add(curr)
            return False

        # Convert start and destination to tuples for consistency
        start, destination = tuple(start), tuple(destination)

        # If the start is the destination, return True immediately
        if start == destination:
            return True

        # Get the number of rows and columns in the maze
        rows, cols = len(maze), len(maze[0])

        # Initialize the visited and visiting sets
        visited, visiting = set(), set()

        # Start the depth-first search from the starting position
        return dfs(start)
