class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        x = abs(fx - sx)
        y = abs(fy - sy)
        
        maxi = max(x, y)
        # print(max)
        if maxi <= t:
            if maxi < t and maxi == 0:
                # print(maxi)
                if t != 1:
                    return True
            else:
                return True
            
        return False
                
                
                
        
        