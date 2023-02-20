class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans =[ [0 for _ in range(n-2)] for _ in range(n-2)]
        maxi = 0
        #  Time compelity is O(N^2) because the size ot the 3 * 3 is always 9       
        
        for row in range(n-2):
            for col in range(n-2):
                maxi = grid[row][col]
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        maxi = max(maxi, grid[i][j])
                        
                ans[row][col] = maxi
                
        return ans
        