class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def inbound(index):
            return 0 <= index < len(nums)
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
       
        if not inbound(high + 1) or nums[high + 1] != target:
            return [-1, -1]
        
        low2 = 0
        high2 = len(nums) - 1
        
        while low2 <= high2:
            mid = low2 + (high2 - low2) // 2
            
            if nums[mid] <= target:
                low2 = mid + 1
            else:
                high2 = mid - 1
                
        
        if not inbound(high2) or nums[high2] != target:
            return [-1, -1]
        
        answer =  [high + 1, high2]
        
        return answer
                
        