class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        start = 0
        mini = float('inf')
        sums = 0
        
        for end in range(length):
            sums += nums[end]
            while sums >= target:
                mini = min(mini, end - start + 1)
                sums -= nums[start]
                start += 1
                
                
        if mini == float('inf'):
            mini = 0
        
            
        return mini
        