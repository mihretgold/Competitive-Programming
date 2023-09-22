class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS = 0
        indexT = 0
        lengthS = len(s)
        lengthT = len(t)
        
        if lengthS == 0:
            return True
        
        while indexS < lengthS and indexT < lengthT:
            if s[indexS] == t[indexT]:
                indexS += 1
            if indexS >= lengthS:
                return True
            
            indexT += 1
            
        return False
        

