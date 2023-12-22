class Solution:
    def maxScore(self, s: str) -> int:
        oneTotal = s.count("1")
        length = len(s)      
        maxx = 0
        oneCount = 0 
        zeroCount = 0
        
        for i in range(length-1):
            oneCount += (s[i] == "1")
            zeroCount += (s[i] == "0")
            
            score = zeroCount + (oneTotal - oneCount)
            maxx = max(score, maxx)
            
            
        return maxx
        
        
        