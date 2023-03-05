class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        mini = float('inf')

        for index in range(length-2, -1, -1):
            grid[0][index] += grid[0][index+1]
        
        for index in range(1, length):
            grid[1][index] += grid[1][index-1]


        for index in range(length):
            choice1 = 0
            if index > 0:
                choice1 = grid[1][index-1]
            choice2 = 0
            if index < length-1:
                choice2 = grid[0][index + 1]
            choice = max(choice1, choice2)
            mini = min(mini, choice)

        return mini