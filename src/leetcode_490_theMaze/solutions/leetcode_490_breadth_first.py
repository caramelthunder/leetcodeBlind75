from collections import deque
from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        """
        Determines if there is a valid path in the maze from the start point to the destination point using Breadth-First Search (BFS).

        Parameters:
        maze (List[List[int]]): A 2D grid representing the maze where 0 indicates an open path and 1 indicates a wall.
        start (List[int]): The starting point represented as [row, col].
        destination (List[int]): The destination point represented as [row, col].

        Returns:
        bool: True if there is a path from start to destination, False otherwise.

        Time Complexity:
        The time complexity is O(m⋅n⋅(m+n)) where m is the number of rows and n is the number of columns in the maze.

        Space Complexity:
        The space complexity is O(m*n) due to the additional space required to store the visited nodes.
        """

        def rolling(
            curr: tuple[int, int], direction: tuple[int, int]
        ) -> tuple[int, int]:
            """Computes the next position in the maze by "rolling" in the given direction until hitting a wall or boundary."""
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

        start, destination = tuple(start), tuple(destination)

        if start == destination:
            return True

        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]
        visited[start[0]][start[1]] = True
        q = deque([start])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            curr_row, curr_col = q.popleft()
            for direction in directions:
                next_row, next_col = rolling((curr_row, curr_col), direction)
                if (
                    not visited[next_row][next_col]
                    and maze[next_row][next_col] == 0
                ):
                    if (next_row, next_col) == destination:
                        return True
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))
        return False
