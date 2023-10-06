class Solution:
    def integerBreak(self, n: int) -> int:
        maxx = 0
        
        for index in range(2, n + 1):
            div = n % index
            val1 = n // index
            val2 = ceil(n/index)
            if div == 0:
                answer = val1 ** index
            else:
                answer = val2 ** div * val1 ** (index - div)
            # print(answer, val1, val2, div)
            
            if answer < maxx:
                break
                
            maxx = answer
            
        return maxx