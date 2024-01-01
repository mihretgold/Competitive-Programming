class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse= True)        
        content = 0
        lengthS = len(s)
        lengthG = len(g)
        child = 0
        cookie = 0
        
        while child < lengthG and cookie < lengthS:
            if s[cookie] >= g[child]:
                cookie += 1
                content += 1
                
            child += 1
            
        return content
            
                