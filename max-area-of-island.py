class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visted = set()
        area = 0
        maxi = 0
        length_row = len(grid)
        length_col = len(grid[0])

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row, col):
            nonlocal area
            visted.add((row, col))
            area += 1

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and (new_row, new_col) not in visted and grid[new_row][new_col]:
                    dfs(new_row, new_col)

        for row in range(length_row):
            for col in range(length_col):
                if grid[row][col] and (row, col) not in visted:
                    dfs(row,col)
                    maxi = max(maxi, area)
                    area = 0

        return maxi