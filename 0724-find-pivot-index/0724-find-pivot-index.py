class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        sums = 0
        for i in range(length):
            sums += nums[i]
        
        p = 0
        for i in range(length):            
            if p*2 == sums - nums[i]:
                return i
            p += nums[i]
        
        return -1