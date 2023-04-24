class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        temp = 0
        temp2 = 0
        visted = set()
        for row in range(length):
            for col in range(length):
                if (row, col) not in visted:
                    visted.add((row, col))
                    new_row = col
                    new_col = (length - row) - 1
                    visted.add((new_row, new_col))
                    temp = matrix[new_row][new_col]
                    matrix[new_row][new_col] = matrix[row][col]
                    r = new_col
                    c = (length - new_row) -1
                    visted.add((r, c))
                    temp2 = matrix[r][c]
                    matrix[r][c] = temp
                    new_row = c
                    new_col = (length - r) -1
                    visted.add((new_row, new_col))
                    temp = matrix[new_row][new_col]
                    matrix[new_row][new_col] = temp2
                    r = new_col
                    c = (length - new_row) -1
                    visted.add((r, c))
                    matrix[r][c] = temp

        return matrix