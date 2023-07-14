class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int: 
        mem = defaultdict(int)
        def calc(row, col):
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                if row -1 == len(matrix)-1:
                    return 0
                else:
                    return float('inf')

            if (row, col) in mem:
                return mem[(row, col)]

            below = matrix[row][col] + calc(row+1, col-1)
            diagonalLeft = matrix[row][col] + calc(row+1, col)
            diagonalRight = matrix[row][col] + calc(row+1, col+1)

            

            mem[(row, col)] = min(below, diagonalLeft, diagonalRight)

            return mem[(row, col)]

        mini = float('inf')
        length = len(matrix)
        for index in range(length):
            mem = defaultdict(int)
            result = calc(0, index)
            mini = min(mini, result)

        

        return mini