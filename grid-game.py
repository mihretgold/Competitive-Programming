class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        suffix = list(accumulate(reversed(grid[0]), initial = 0))
        prefix = list(accumulate(grid[1], initial = 0))
        suffix.reverse()
        mini = float('inf')

        for index in range(length):
            choice1 = prefix[index]
            choice2 = suffix[index + 1]
            choice = max(choice1, choice2)
            mini = min(mini, choice)
            
        return mini