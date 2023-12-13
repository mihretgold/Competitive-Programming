class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        transponse = list(map(list, zip(*mat)))
        visted = set()
        lengthR = len(mat)
        lengthC = len(mat[0])
        answer = 0
        
        for i in range(lengthR):
            for j in range(lengthC):
                total = mat[i].count(1) + transponse[j].count(1) - mat[i][j]
                if total == 1 and mat[i][j] == 1:
                    answer += 1
                    
        
        return answer