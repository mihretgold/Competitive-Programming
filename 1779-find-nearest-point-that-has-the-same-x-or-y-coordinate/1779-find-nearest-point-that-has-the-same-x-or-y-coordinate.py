class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        Manhattan = float('inf')
        length = len(points)
        index = -1
        
        for cordinate in range(length):
            if points[cordinate][0] == x or  points[cordinate][1] == y:
                num = abs(x - points[cordinate][0]) + abs(y - points[cordinate][1])
                if num < Manhattan:
                    Manhattan = num
                    index = cordinate
                    
        return index