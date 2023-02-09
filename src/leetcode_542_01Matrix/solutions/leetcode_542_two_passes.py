class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        R, C = len(mat), len(mat[0])

        for row in range(R):
            for col in range(C):
                if mat[row][col] != 0:
                    top = mat[row - 1][col] if row - 1 >= 0 else float("inf")
                    left = mat[row][col - 1] if col - 1 >= 0 else float("inf")
                    mat[row][col] = min(top, left) + 1
                    
        for row in range(R - 1, -1, -1):
            for col in range(C - 1, -1, -1):
                if mat[row][col] != 0:
                    bottom = mat[row + 1][col] if row + 1 < R else float("inf")
                    right = mat[row][col + 1] if col + 1 < C else float("inf")
                    mat[row][col] =  min(mat[row][col], min(bottom, right) + 1)

        return mat