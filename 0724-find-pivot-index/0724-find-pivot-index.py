class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0 for _ in range(length)]
        prefix[0] = nums[0]
        for i in range(1, length):
            prefix[i] = prefix[i-1] + nums[i]
        
        suffix = [0 for _ in range(length)]
        suffix[length-1] = nums[-1]
        
        for i in range(length-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]
            
        for i in range(length):
            if prefix[i] == suffix[i]:
                return i
        
        return -1