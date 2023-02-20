class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if r * c != n * m:
            return mat
        
        store = []
        ans = [ [0 for _ in range(c)] for _ in range(r)]
        
        for i in range(n):
            for j in range(m):
                store.append(mat[i][j])
                
        index = 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = store[index]
                index += 1
                
        return ans
            
                
        
        