class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        LEFT, RIGHT = 0, len(matrix[0]) - 1
        UP, DOWN = 0, len(matrix) - 1
        
        n = (RIGHT - LEFT + 1) * (DOWN - UP + 1)
        output = []

        while len(output) < n:

            for col in range(LEFT, RIGHT + 1):
                output.append(matrix[UP][col])

            for row in range(UP + 1, DOWN + 1):
                output.append(matrix[row][RIGHT])

            if UP != DOWN:
                for col in range(RIGHT - 1, LEFT - 1, -1):
                    output.append(matrix[DOWN][col])

            if LEFT != RIGHT:
                for row in range(DOWN - 1, UP, -1):
                    output.append(matrix[row][LEFT])

            LEFT += 1
            RIGHT -= 1
            UP += 1
            DOWN -= 1

        return output