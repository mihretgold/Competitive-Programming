class Solution:
    def knightDialer(self, n: int) -> int:

        matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['-1', '0', '-1']]

        def inbound(row, col):
            return 0 <= row < 4 and 0 <= col < 3
        
        direction = [(2, 1), (-2, 1), (-2, -1), (2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

        @cache
        def dp(row, col, count):
            if not inbound(row, col) or matrix[row][col] == '-1':
                return 0

            if count >= n:                
                return 1

            answer = 0
            for newRow, newCol in direction:
                newRow += row
                newCol += col
                
                answer += dp(newRow, newCol, count + 1)
                    
            return answer % (10**9 + 7)

        answer = 0
        for row in range(4):
            for col in range(3):
                if matrix[row][col] != '-1':
                    answer += dp(row, col, 1)

        return answer % (10**9 + 7)