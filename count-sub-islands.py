class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        length_row = len(grid2)
        length_col = len(grid2[0])

        def inbound(row, col):
            return (0 <= row < len(grid2)) and (0 <= col < len(grid2[0]))

        def dfs(row, col):
            sub_islands = True
            grid2[row][col] = 0
            if not grid1[row][col]:
                sub_islands = False

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid2[new_row][new_col]== 1:
                    sub_islands &= dfs(new_row, new_col)                        

            return sub_islands
        
        result = 0
        for row in range(length_row):
            for col in range(length_col):
                if grid2[row][col]:
                    if dfs(row, col):
                        result += 1

        return result