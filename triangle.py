class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mem = defaultdict(int)
        def calcMin(row, col):
            if row >= len(triangle):
                return 0

            if (row, col) in mem:
                return mem[(row, col)]

            left = calcMin(row+1, col) + triangle[row][col]
            right = calcMin(row+1, col+1) + triangle[row][col]
            
            mem[(row, col)] = min(right, left)
            
            return mem[(row, col)]

        return calcMin(0, 0)