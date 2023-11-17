class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visted = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = 0
        length_row = len(grid)
        length_col = len(grid[0])

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row, col):
            nonlocal result
            if not inbound(row, col) or grid[row][col] == 0:
                result += 1
                return

            visted.add((row, col))

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if (new_row, new_col) not in visted:
                    dfs(new_row, new_col)

        for row in range(length_row):
            for col in range(length_col):
                if grid[row][col] == 1 and (row, col) not in visted:
                    dfs(row, col)

        return result


            
            