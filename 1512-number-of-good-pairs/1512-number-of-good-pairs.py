class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        right = 0
        left = 1
        count = 0
        length = len(nums)
        
        while(right < length-1):
            if nums[right] == nums[left]:
                count += 1
            if left == length -1:
                right += 1
                left = right
            left += 1
        
        return count