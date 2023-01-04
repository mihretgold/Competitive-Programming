class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_size = len(grid)
        row_size = len(grid[0])
        
        map_row = defaultdict(int)
        map_col = defaultdict(int)
        
        for col in range(col_size):
            temp = tuple(grid[col])
            map_row[temp] += 1
            
        for col in range(col_size):
            col_temp = []
            for row in range(col_size):
                col_temp.append(grid[row][col])
            temp = tuple(col_temp)
            map_col[temp] += 1
        
        count = 0
        for arr in map_row:
            add = map_col[arr] * map_row[arr]
            count += add
        
        return count
                
                