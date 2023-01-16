class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row_length = len(strs)
        col_length = len(strs[0])
        count = 0
        for col in range(col_length):
            for row in range(row_length-1):
                if strs[row][col] > strs[row + 1][col]:
                    count += 1
                    break
                    
        return count