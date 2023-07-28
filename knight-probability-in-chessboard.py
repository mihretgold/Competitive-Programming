class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]

        def inbound(row, col):
            return (0 <= row < n) and (0 <= col < n)

        mem = defaultdict(int)
        def calcProbablity(moves, row, col):
            if not inbound(row, col):
                return 0

            if moves == 0:
                return 1

            if (moves, row, col) in mem:
                return mem[(moves, row, col)]

            count = 0

            for newRow, newCol in directions:
                newRow += row
                newCol += col
                count += calcProbablity(moves - 1, newRow, newCol)/8

            mem[(moves, row, col)] = count
            return mem[(moves, row, col)]            
        
        return calcProbablity(k, row, column)