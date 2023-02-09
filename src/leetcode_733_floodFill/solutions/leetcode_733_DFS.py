class Solution:
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