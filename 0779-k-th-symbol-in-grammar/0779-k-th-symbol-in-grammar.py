class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        val = self.kthGrammar(n - 1, math.ceil(k/2))
        
        if val == 0:
            if k & 1 ==  0:
                return 1
            else:
                return 0
        else:
            if k & 1 ==  0:
                return 0
            else:
                return 1
        
        