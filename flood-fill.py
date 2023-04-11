class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mark = image[sr][sc]
        visted = set()

        def inbound(row, col):
            return (0 <= row < len(image)) and (0 <= col < len(image[0]))

        def dfs(row, col): 
            nonlocal mark
            visted.add((row, col))
            image[row][col] = color


            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and image[new_row][new_col] == mark and (new_row, new_col) not in visted:
                    dfs(new_row, new_col)
            
            return

        dfs(sr, sc)
        return image