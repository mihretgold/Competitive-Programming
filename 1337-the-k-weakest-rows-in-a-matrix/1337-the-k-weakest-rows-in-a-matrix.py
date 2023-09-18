class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        length = len(mat)
        soldierCount = []
        
        for row in range(length):
            soldiers = mat[row].count(1)
            soldierCount.append((soldiers, row))
            
        soldierCount.sort()
        answer = []
        
        for index, val in enumerate(soldierCount):
            if index < k:
                answer.append(val[1])
            else:
                break
                
        return answer
            
                
        
        
        
        