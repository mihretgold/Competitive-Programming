class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        length_row = len(grid)
        length_col = len(grid[0])
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row, col):
            grid[row][col] = "0"

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col - col_change

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)

        island = 0
        for row in range(length_row):
            for col in range(length_col):
                if grid[row][col] == "1":
                    dfs(row, col)
                    island += 1

        return island