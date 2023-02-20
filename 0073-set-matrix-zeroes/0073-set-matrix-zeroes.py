class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_size = len(matrix)
        col_size = len(matrix[0])
        
        set_row = set()
        set_col = set()
        for row in range(row_size):
            for col in range(col_size):
                if matrix[row][col] == 0:
                    set_row.add(row)
                    set_col.add(col)
        for row in range(row_size):
            for col in range(col_size):
                if row in set_row or col in set_col:
                    matrix[row][col] = 0
                    
                    