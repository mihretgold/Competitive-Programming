class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        length = len(nums)
        increasing = True 
        decreasing = True

        for i in range(length-1):
            increasing &=  nums[i] >= nums[i+1]
            decreasing &= nums[i] <= nums[i+1]
        
        result = increasing or decreasing
        
        return result