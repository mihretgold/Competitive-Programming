class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0 for _ in range(length+1)]
        prefix[0] = 0
        for i in range(1, length+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        
        for i in range(length):
            check = prefix[-1] - prefix[i+1]
            if prefix[i] == check:
                return i        
        
        return -1