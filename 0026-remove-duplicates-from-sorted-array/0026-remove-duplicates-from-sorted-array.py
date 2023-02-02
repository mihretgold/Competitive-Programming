class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        length = len(nums)
        for right in range(length):
            if nums[right] != nums[left]:
                nums[left+1] = nums[right]
                left += 1
                
        return left+1