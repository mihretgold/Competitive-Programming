class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_count = []
        col_count = []
        size = 0
        length = len(grid)  
        for col in range(length):
            sum = 0
            size = len(grid[0])
            for row in range(size):
                if grid[col][row] == 1:
                    sum += grid[col][row]
            row_count.append(sum)        
       
        for col in range(size):
            sum = 0
            size = len(grid[0])
            for row in range(length):
                if grid[row][col] == 1:
                    sum += grid[row][col]
            col_count.append(sum)
            
        diff = []   
        for row in range(length):
            rsize = len(col_count)
            temp = []
            for col in range(rsize):
                num = row_count[row] + col_count[col] - (rsize - row_count[row]) - (length - col_count[col])
                temp.append(num)
            diff.append(temp)
        
        return diff
                
                    