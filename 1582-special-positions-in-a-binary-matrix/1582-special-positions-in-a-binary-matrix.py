class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        lengthR = len(mat)
        lengthC = len(mat[0])
        answer = 0
        rowSum = []
        colSum = []
        
        for row in range(lengthR):
            total = sum(mat[row])
            rowSum.append(total)
            
        for col in range(lengthC):
            total = 0
            for row in range(lengthR):
                total += mat[row][col]
                
            colSum.append(total)
       
        
        for row in range(lengthR):
            for col in range(lengthC):
                if mat[row][col]:
                    check = (rowSum[row] - 1) + (colSum[col] - 1)
                    if not check:
                        answer += 1
                    
        
        return answer