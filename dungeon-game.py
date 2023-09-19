class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        lengthRow, lengthCol = len(dungeon), len(dungeon[0])
        if dungeon[lengthRow - 1][lengthCol - 1] > 0:
            dungeon[lengthRow -1][lengthCol- 1] = 0

        for row in range(lengthRow - 1, -1, -1):
            for col in range(lengthCol-1, -1, -1):
                if (row, col) == (lengthRow-1, lengthCol - 1): continue
                right = float('-inf')
                down = float('-inf')
   
                if row + 1 < lengthRow:
                    down = dungeon[row + 1][col]
                
                if col + 1 < lengthCol:
                    right = dungeon[row][col+1]

                maxi = max(right, down)
                if maxi > 0:
                    maxi = 0
                answer = dungeon[row][col] + maxi
                if answer > 0:
                    answer = 0

                dungeon[row][col] = answer 

        return abs(dungeon[0][0]) + 1