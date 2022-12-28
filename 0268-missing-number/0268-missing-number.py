class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        for index in range(length):
            if index not in nums:
                 return index