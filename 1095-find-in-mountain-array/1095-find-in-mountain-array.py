# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low = 1
        length = mountain_arr.length()
        high = length - 2
        store = [-1] * length
        peak = 0
        
        while low <= high:
            mid = low + (high - low)//2
            
            if store[mid] == -1:                
                getMid = mountain_arr.get(mid)
                store[mid] = getMid
            else:
                getMid = store[mid]
            if store[mid - 1] == -1:                
                getMinus = mountain_arr.get(mid-1)
                store[mid-1] = getMinus
            else:
                getMinus = store[mid-1]
                
            if store[mid + 1] == -1:                
                getPlus = mountain_arr.get(mid + 1)
                store[mid + 1] = getPlus
            else:
                getPlus = store[mid + 1]
            
            if getMinus <  getMid > getPlus:
                peak = mid
                break
            elif getMinus < getMid < getPlus:
                low = mid + 1
            elif getMinus > getMid > getPlus:
                high = mid - 1
                
        low = 0
        high = peak
        found = -1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if store[mid] == -1:
                val = mountain_arr.get(mid)
                store[mid] = val
            else:
                val = store[mid]
                
            if val == target:
                found = mid
                break
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        if found != -1:
            return found
        low = peak + 1
        high = length - 1
        found = -1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if store[mid] == -1:
                val = mountain_arr.get(mid)
                store[mid] = val
            else:
                val = store[mid]
                
            if val == target:
                found = mid
                break
            elif val > target:
                low = mid + 1
            else:
                high = mid - 1
                
                
        return found 