class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        ans = length
        nums = sorted(set(nums))
     
        j = 0
        for index, num in enumerate(nums):
            while j < len(nums) and nums[j] < num + length:
                j += 1

            val = j - index 
            ans = min(ans, length - val)
                
        return ans