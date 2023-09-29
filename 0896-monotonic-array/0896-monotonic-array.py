class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        arr = nums[:]
        arr.sort()
        if nums == arr:
            return True
        if arr[::-1] == nums:
            return True
        
        return False
        