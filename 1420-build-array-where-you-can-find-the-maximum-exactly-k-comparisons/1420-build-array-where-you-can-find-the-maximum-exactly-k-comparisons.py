class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        count = 0
        @cache
        def bt(nums, searchCount, maxx): 
            if nums == n:
                if searchCount == 0:
                    return 1
                return 0
            
            
            answer = (maxx *  bt(nums + 1, searchCount, maxx)) % (10 ** 9 + 7)
            for idx in range(maxx + 1, m + 1):
                answer = (answer + bt(nums + 1, searchCount - 1, idx)) % (10 ** 9 + 7)
                
                    
                    
            return answer
                  
            
        
        count = bt(0, k, 0)
        return count % (10 ** 9 + 7) 

                    
        