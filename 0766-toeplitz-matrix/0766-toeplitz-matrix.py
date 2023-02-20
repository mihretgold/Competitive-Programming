class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        col_size = len(matrix[0])
        row_size = len(matrix)
        
        
        for row in range(1, row_size):
            for col in range(1, col_size):
                if matrix[row - 1][col - 1] != matrix[row][col]:
                    return False
                      
        return True