'''
https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
        1 1 1
        1 1 0
        1 0 1
Output: [[2,2,2],[2,2,0],[2,0,1]]
        2 2 2
        2 2 0
        2 0 1
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 
Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
'''

class DFS_Solution:
    def floodFill(self, image: list[int], sr: int, sc: int, color: int) -> list[list[int]]:
        R, C = len(image), len(image[0])

        def dfs(image, row, col, current_color):
            image[row][col] = color

            for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = _r + row
                new_col = _c + col

                if R > new_row >= 0 and C > new_col >= 0 and image[new_row][new_col] == current_color:
                    dfs(image, new_row, new_col, current_color)

        current_color = image[sr][sc]
        if current_color != color:
            dfs(image, sr, sc, current_color)

        return image

from collections import deque
class BFS_Solution:
    def floodFill(self, image: list[int], sr: int, sc: int, color: int) -> list[list[int]]:
        R, C = len(image), len(image[0])
        current_color = image[sr][sc]

        if current_color == color:
            return image

        q = deque([(sr, sc)])
        while q:
            row, col = q.popleft()
            image[sr][sc] = color
            for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = _r + row
                new_col = _c + col

                if R > new_row >= 0 and C > new_col >= 0 and image[new_row][new_col] == current_color:
                    q.append((new_row, new_col))

        return image

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.dfs_solution = DFS_Solution()
        self.bfs_solution = BFS_Solution()
    
    def test_example1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr, sc, color = 1, 1, 2
        expected_output = [[2,2,2],[2,2,0],[2,0,1]]

        actual_output_dfs = self.dfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_dfs, expected_output)
        actual_output_bfs = self.bfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_bfs, expected_output)

    def test_example2(self):
        image = [[0,0,0],[0,0,0]]
        sr, sc, color = 0, 0, 0
        expected_output = [[0,0,0],[0,0,0]]

        actual_output_dfs = self.dfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_dfs, expected_output)
        actual_output_bfs = self.bfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_bfs, expected_output)

    def test_empty_grid(self):
        # Test starting pixel at the corner of the grid
        self.assertEqual(self.dfs_solution.floodFill([[0, 1], [1, 1]], 0, 0, 2), [[2, 1], [1, 1]])
        self.assertEqual(self.bfs_solution.floodFill([[0, 1], [1, 1]], 0, 0, 2), [[2, 1], [1, 1]])

    def test_same_color(self):
        self.assertEqual(self.dfs_solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 1), [[1,1,1],[1,1,0],[1,0,1]])
        self.assertEqual(self.bfs_solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 1), [[1,1,1],[1,1,0],[1,0,1]])
        
    #######################################
if __name__ == '__main__':
    unittest.main()